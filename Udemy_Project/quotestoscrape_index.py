import requests
from bs4 import BeautifulSoup

website = requests.get('https://quotes.toscrape.com/')

soup = BeautifulSoup(website.text, 'html.parser')

quote = soup.find(class_='text')

print(quote.text)


