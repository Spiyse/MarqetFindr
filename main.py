from bs4 import BeautifulSoup
import requests

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
listing_num = 1
for listing_table_row in listing_table_rows:
    # d1 is the listings title or name or whatever
    listing_num += 1
    title_div = listing_table_row.find('div', class_='d1')
    if title_div:
        title_link = title_div.find('a')
        title_text = (title_link.get_text(strip=True) if title_link else title_div.get_text(strip=True))
        if title_text:
            listing_names.append(title_text)


