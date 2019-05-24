import requests 
from bs4 import BeautifulSoup
import re 

def craigslist(num):
        result = requests.get("https://montreal.craigslist.org/search/apa?max_price=1100&availabilityMode=0&sale_date=all+dates&lang=en&cc=us")
        html_doc = result.content
        soup = BeautifulSoup(html_doc, 'html.parser')
        LINKS = []
        for link in soup.find_all('a'):
                l = link.get('href')
                match = re.search("^https://montreal.craigslist.org/apa/d/",l)
                if(match):
                        LINKS.append(l)

        LINKS = list(dict.fromkeys(LINKS))

        APTS = []
        for i in range(0, num):
                apt = requests.get(LINKS[i])
                apt_doc = apt.content
                apt_soup = BeautifulSoup(apt_doc, 'html.parser')
                price = apt_soup.find(class_="price")
                geo = apt_soup.find(class_="viewposting")
                apartment = {
                        "name"  : apt_soup.title.text,
                        "price" : int(price.text[1:]),
                        "url"   : LINKS[i],
                        "coords" : [float(geo['data-latitude']), float(geo['data-longitude'])],
                        "metro" : None,
                        "distance" : None
                        }
                APTS.append(apartment)
        return APTS
