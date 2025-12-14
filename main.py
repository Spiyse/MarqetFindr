from bs4 import BeautifulSoup
import requests
from marqet_findr.core.utils import extract_text

url = 'https://www.ss.com/lv/electronics/computers/pc/'

page = requests.get(url)
page.raise_for_status()

soup = BeautifulSoup(page.text, features='html.parser')

tables = soup.find_all('table')
if len(tables) < 2:
    print("No listings table found")
    exit(1)

listing_table = tables[1]
listing_table_rows = listing_table.find_all('tr')


listing_names = []
listing_prices = []
listing_regions = []

for listing_table_row in listing_table_rows:
    # d1 is the listings title or name or whatever
    # ampot is the listings price
    # ads_region is the listings region/location

    title_div = listing_table_row.find('div', class_='d1')
    price_td = listing_table_row.select_one('td:nth-of-type(7)')
    region_div = listing_table_row.find('div', class_='ads_region')

    if price_text := extract_text(price_td, 'a', 'ampot'):
        listing_prices.append(price_text)

    if title_text := extract_text(title_div, 'a'):
        listing_names.append(title_text)

    if region_text := extract_text(region_div):
        listing_regions.append(region_text)

    

print(listing_names[1])
print(listing_prices[1])
print(listing_regions[1])

