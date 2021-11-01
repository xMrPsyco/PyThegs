import requests
from bs4 import BeautifulSoup
import pandas as pd

#url = 'https://www.amazon.nl/-/en/product-reviews/B08J6VTK6B/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber=1'
reviewlist = []


def get_soup(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text,  'html.parser')
    return soup

def get_reviews(soup):

    reviews = soup.find_all('div', {'data-hook': 'review'})
    try:
        for item in reviews:
            review = {
            'product': soup.title.text.replace('Amazon.co.uk:Customer reviews:', '').strip(), #If you want to use this for other amazon website like .nl or .de, change te text to Amazon.nl/de:Customer reviews. Otherwise the script will not work.
            'title': item.find('a', {'data-hook':  'review-title'}).text.strip(), #strip removes al white spaces.
            'rating':  float(item.find('i', {'data-hook': 'review-star-rating'}).text.replace('out of 5 stars', '').strip()), #this replaces the text with nothing, because we only want the first numbers.
            'body': item.find('span', {'data-hook': 'review-body'}).text.strip(),
            }
            reviewlist.append(review)
    except:
        pass

for x in range(1,10): #x replaces the numbers so we can get different review pages
    soup = get_soup(f'https://www.amazon.co.uk/product-reviews/B07PZR3PVB/ref=cm_cr_arp_d_paging_btm_next_2?ie=UTF8&reviewerType=all_reviews&pageNumber={x}') #REPLACE THIS URL WITH THE ONE YOU WANT. GO TO THE PRODUCT PAGE, SCROLL DOWN AND CLICK ON AL REVIEWS, THEN CLICK ON THE NEXT PAGE. EXTRACT THE URL WITHOUT THE NUMBER ON THE END AFTER =.
    print(F'Getting Page: {x}')
    get_reviews(soup)
    print(len(reviewlist))
    if not soup.find('li', {'class': 'a-disabled a-last'}):
        pass
    else:
        break #this stops the loop (script)

df = pd.DataFrame(reviewlist)
df.to_csv('airpods.csv', index=False)
print('Done.')










