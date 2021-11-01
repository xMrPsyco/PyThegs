import requests
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')

print(website.text)