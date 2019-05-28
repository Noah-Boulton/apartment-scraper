import requests
import re
from bs4 import BeautifulSoup
from distance import closest_metro

def get_kijiji_links():
        result = requests.get('https://www.kijiji.ca/b-appartement-condo/grand-montreal/c37l80002?price=0__1100&ad=offering')
        html_doc = result.content
        soup = BeautifulSoup(html_doc, 'html.parser')

        LINKS = []
        for link in soup.find_all('a'):
                l = link.get('href')
                match = re.search("\/v-appartement-condo\/ville-de-montreal\/.*\/\d+$", str(l))
                if(match):
                        LINKS.append("https://www.kijiji.ca" + l)

        LINKS = list(dict.fromkeys(LINKS))
        return LINKS

def get_kijiji_listings(link):
        apt = requests.get(link)
        apt_doc = apt.content
        apt_soup = BeautifulSoup(apt_doc, 'html.parser')
        latitude = apt_soup.find("meta",  property="og:latitude")
        longitude = apt_soup.find("meta",  property="og:longitude")
        coords = [float(latitude['content']), float(longitude['content'])]
        price = re.search("'price', value: '(\d{3,4})'", str(apt_soup))
        metro = closest_metro(coords)
        apartment = {
                "name"  : apt_soup.title.text,
                "price" : int(price.group(1)) if price else 0,
                "url"   : link,
                "coords" : coords,
                "metro" : metro[0],
                "distance" : metro[1]
                }
        return apartment
