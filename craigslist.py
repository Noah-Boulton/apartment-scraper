import requests 
import re 
from bs4 import BeautifulSoup
from distance import area

def get_craigslist_links():
        result = requests.get("https://vancouver.craigslist.org/search/apa?max_price=2500&min_bedrooms=2&minSqft=850&availabilityMode=0&sale_date=all+dates")
        html_doc = result.content
        soup = BeautifulSoup(html_doc, 'html.parser')

        LINKS = []
        for link in soup.find_all('a'):
                l = link.get('href')
                match = re.search("^https://vancouver.craigslist.org/\w\w\w/apa/d/",l)
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
        if(geo is None):
                return None
        coords = [float(geo['data-latitude']), float(geo['data-longitude'])]
        neighbourhood = area(coords)
        apartment = {
                "name"  : apt_soup.title.text,
                "price" : price,
                "url"   : link,
                "coords" : coords,
                "area" : neighbourhood,
                }
        return apartment
