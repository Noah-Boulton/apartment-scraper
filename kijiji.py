import requests
import re
from bs4 import BeautifulSoup
from distance import area

def get_kijiji_links():
        result = requests.get('https://www.kijiji.ca/b-for-rent/greater-vancouver-area/c30349001l80003?ad=offering&price=__2500')
        html_doc = result.content
        soup = BeautifulSoup(html_doc, 'html.parser')

        LINKS = []
        for link in soup.find_all('a'):
                l = link.get('href')
                match = re.search("\/(v-apartments-condos|v-house-rental)\/.+\/.+\/\d+$", str(l))
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
        neighbourhood = area(coords)
        apartment = {
                "name"  : apt_soup.title.text,
                "price" : int(price.group(1)) if price else 0,
                "url"   : link,
                "coords" : coords,
                "area" : neighbourhood
                }                
        return apartment
