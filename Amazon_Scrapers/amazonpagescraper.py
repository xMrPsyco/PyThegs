from requests_html import HTMLSession
from bs4 import BeautifulSoup

s = HTMLSession()

url = 'https://www.amazon.nl/s?k=charger&i=black-friday&ref=nb_sb_noss_2' #replace the link here

def getdata(url):
    r = s.get(url)
    r.html.render(sleep=1)
    soup = BeautifulSoup(r.html.html, 'html.parser')
    return soup

def getnextpage(soup):
    page = soup.find('ul', {'class': 'a-pagination'})
    if not page.find('li', {'class': 'a-disabled a last'}):
        url = 'http://www.amazon.nl' + str(page.find('li',{'class':'a-last'}).find('a')['href'])
        return url
    else:
        return


while True:
    data = getdata(url)
    url = getnextpage(data)
    if not url:
        break
    print(url)
    








