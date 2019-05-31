import requests 
import re 
from bs4 import BeautifulSoup
from distance import closest_metro

def get_craigslist_links():
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
        return LINKS

def get_craigslist_listings(link):
        apt = requests.get(link)
        apt_doc = apt.content
        apt_soup = BeautifulSoup(apt_doc, 'html.parser')
        price = apt_soup.find(class_="price")
        if(price):
                price = int(price.text[1:])
        geo = apt_soup.find(class_="viewposting")
        coords = [float(geo['data-latitude']), float(geo['data-longitude'])]
        metro = closest_metro(coords)
        apartment = {
                "name"  : apt_soup.title.text,
                "price" : price,
                "url"   : link,
                "coords" : coords,
                "metro" : metro[0],
                "distance" : metro[1]
                }
        return apartment
