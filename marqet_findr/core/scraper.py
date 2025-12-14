from bs4 import BeautifulSoup
import requests
import time


def fetch_page(url, config=None):
    # Fetch a webpage with optional config for headers, timeout, and retries
    if config is None:
        config = {}
    
    scraping_config = config.get('scraping', {})
    timeout = scraping_config.get('timeout', 10)
    headers = scraping_config.get('headers', {})
    retry_attempts = scraping_config.get('retry_attempts', 1)
    
    for attempt in range(retry_attempts):
        try:
            page = requests.get(url, timeout=timeout, headers=headers)
            page.raise_for_status()
            return BeautifulSoup(page.text, features='html.parser')
        except requests.RequestException as error:
            if attempt < retry_attempts - 1:
                time.sleep(1)
                continue
            raise error
