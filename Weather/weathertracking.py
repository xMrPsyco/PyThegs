from requests_html import HTMLSession

s = HTMLSession()

query = 'Tilburg' #if you put a location in here, it will adjust in the code and extract the weather
url = f'https://www.google.com/search?q=weather+{query}'

#import your  user agent down here (search on google: my user agent) copy and paste it.
r = s.get(url, headers={'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36'}) #this makes sure you past the google ai bot

temperature = r.html.find('span#wob_tm', first=True).text
unit =  r.html.find('div.vk_bk.wob-unit span.wob_t', first=True).text
desc = r.html.find('div.VQF4g', first=True).find('span#wob_dc', first=True).text

print (query, temperature, unit, desc)







