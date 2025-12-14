from marqet_findr.core.utils import extract_text


def parse_listings(soup, config=None):
    if config is None:
        config = {}
    
    parsing_config = config.get('parsing', {})
    table_index = parsing_config.get('table_index', 1)
    
    tables = soup.find_all('table')
    if len(tables) < table_index + 1:
        return []

    listing_table = tables[table_index]
    listing_table_rows = listing_table.find_all('tr')

    listings = []

    for listing_table_row in listing_table_rows:
        # d1 is the listings title or name or whatever
        # ampot is the listings price (always last td)
        # ads_region is the listings region/location
        # foto_list is the listings image

        title_div = listing_table_row.find('div', class_='d1')
        all_tds = listing_table_row.find_all('td')
        price_td = all_tds[-1] if all_tds else None  # Get last td so i can get price
        region_div = listing_table_row.find('div', class_='ads_region')
        image_td = listing_table_row.select_one('td:nth-of-type(2)')

        listing = {}

        if price_text := extract_text(price_td, 'a', 'ampot'):
            listing['price'] = price_text

        if title_text := extract_text(title_div, 'a'):
            listing['name'] = title_text

        if region_text := extract_text(region_div):
            listing['region'] = region_text

        if image_td and (img_tag := image_td.find('img', class_='foto_list')):
            if src := img_tag.get('src'):
                listing['image'] = src

        # Only append if the listing has at least a name
        if listing.get('name'):
            listings.append(listing)

    return listings
