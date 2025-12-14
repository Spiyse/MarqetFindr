from marqet_findr.core import fetch_page, parse_listings
from marqet_findr.config import load_config

# Load configuration
config = load_config()

# Build URL from config
base_url = config.get('base_url')
category = config.get('category') # For now the default catagory is pc's
url = base_url + category

# Fetch the page
soup = fetch_page(url, config)


# Parse listings
listings = parse_listings(soup, config)

if not listings:
    print("No listings found")
    exit(1)

# Display a sample listing for now in the terminal so i can see if the listing info is right
if len(listings) > 1:
    sample = listings[1]
    print(f"Name: {sample.get('name')}")
    print(f"Price: {sample.get('price')}")
    print(f"Region: {sample.get('region')}")
    print(f"Image: {sample.get('image')}")

