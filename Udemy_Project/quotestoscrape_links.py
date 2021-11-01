import requests
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(website.text, 'html.parser')

links = soup.find_all ('a')

for link in links:
    print(link.text)