from bs4 import BeautifulSoup 
import requests
import pandas as pd #Panda's is used for to extract the data into a csv

URL = 'https://en.wikipedia.org/wiki/List_of_largest_manufacturing_companies_by_revenue'
response = requests.get(URL)
soup = BeautifulSoup(response.text, 'html.parser') #gets the HTML

table = soup.find('table', {'class':'wikitable sortable plainrowheads'}).tbody #Looking for the table with BS

rows = table.find_all('tr') #Get's every data that is under 'tr' in the html

columns = [v.text.replace('\n', '') for v in rows[0].find_all('th')] # replaces the text to keep a overview and scrape everything under 'th' in the html

df = pd.DataFrame(columns=columns) #add columns with Panda's

for i in range(1, len(rows)):
    tds = rows[i].find_all('td')

    if len(tds) ==4:
        values = [tds[0].text, tds[1].text, ''. tds[2].text, tds[3].text.replace('\n', '').replace('\xa0','')]
    else:
        values = [td.text.replace('\n', '').replace('\xa0','') for td in tds]


    df = df.append(pd.Series(values, index=columns), ignore_index=True)

    print(df)

    df.to_csv('hobieisgoingtobeexcitedwhenrunningthisscript.csv') #here you can give the file a name. After that RUN IT :P 




















 





















