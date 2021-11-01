import requests
from bs4 import BeautifulSoup 
import smtplib #enables to send emails
import time 

URL = 'https://www.amazon.nl/-/en/dp/B08J6VTK6B/ref=sr_1_5?dchild=1&keywords=Apple%2Bwatch%2Bse&qid=1634753461&sr=8-5&th=1'

headers = {"User-Agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'} #FILL IN YOUR OWN USER AGENT CHECK GOOGLE

def check_price():

    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

#print(soup.prettify()) #Print this and you see the HTML code

    title = soup.find (id="productTitle").get_text()
    price = soup.find ('span', {'class': 'a-offscreen'}).get_text()
    converted_price = float(price[1:4]) #this checks the  first numbers of the price (so it does not extract the . and €) 
    if(converted_price < 286):
        send_mail()

    print(converted_price)
    print(title.strip())

    if(converted_price < 283):
        send_mail() 

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo # ehlo is a command sent by an email server to identify itselfs when connecting to another email server
    server.starttls()
    server.ehlo()

# FILL IN YOUR OWN MAIL/PASSWORD OTHERWISE IT WONT WORK
    server.login('yourgmail@here.com', 'passwordhere') #HERE
    
    subject = 'Price fell down!'
    body = 'Check deze link https://www.amazon.nl/-/en/dp/B08J6VTK6B/ref=sr_1_5?dchild=1&keywords=Apple%2Bwatch%2Bse&qid=1634753461&sr=8-5&th=1 '

    msg = f"Subject: {subject}\n\n{body}"
    
    server.sendmail(
        'yourmail@here.com', #HERE
        'themailyouwantosendit@.com', #HERE
        msg
    )
    print('EMAIL HAS BEEN SEND')

    server.quit()

check_price()

while(True):
    check_price()
    time.sleep(60) #causes the script to be rerun every minute






