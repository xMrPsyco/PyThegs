from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from bs4 import BeautifulSoup
import requests
import time
import csv

driver = webdriver.Chrome('/Users/thijsesch/Documents/scalperbot/chromedriver') #LOCATE YOUW OWN DRIVER DOWNLOAD IT HERE https://chromedriver.chromium.org/downloads *CHECK IN YOUR CHROME BROWSER WHAT VERSION YOU HAVE.

driver.get('https://www.nike.com')

inputElement = driver.find_element_by_id('VisualSearchInput') #Clicks on the search writing place
inputElement.send_keys('air force 1') #Types in the keyword
time.sleep(2)  #let the task wait for 2 second (bot protection)

inputElement.send_keys(Keys.ENTER) #clicks on enter
time.sleep(2) #let the task wait for 2 second (bot protection)

url = driver.current_url
r = requests.get(url).text

soup = BeautifulSoup(r, 'html.parser') #get the html code and from here it start scraping the html code.

shoe_name, gender, price, link = [],[],[],[] #define the columns for the csv  
for tag in soup.find_all('div', attrs={'class': 'product-card__title'}): #filterin shoename
    shoe_name.append(tag.text)
for tag in soup.find_all('div', attrs={'class': 'product-card__subtitle'}): #filtering gender
    gender.append(tag.text)
for tag in soup.find_all('div', attrs={'data-test':'product-price'}): #filterin product price
    price.append(tag.text)

fields = ['Shoe Name', 'Gender', 'Price'] #creates the csv
with open('AF1 Prices.csv', 'w',) as myfile:
    wr = csv.writer(myfile,quoting=csv.QUOTE_ALL)
    wr.writerow(fields)
    for i in range(0,len(shoe_name)):
        s = shoe_name[i]
        g = gender[i]
        p = price[i]
        wr.writerow([s,g,p,])

driver.quit()
print ('Sucess')





    

        




