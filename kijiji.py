import requests
import re
from bs4 import BeautifulSoup

result = requests.get('https://www.kijiji.ca/b-appartement-condo/grand-montreal/c37l80002?price=0__1100&ad=offering')
html_doc = result.content

soup = BeautifulSoup(html_doc, 'html.parser')

# /v-appartement-condo/ville-de-montreal/3-1-2-metro-cote-vertu-tout-inclus-chauffage-electrique/1380288429
# four /

LINKS = []
for link in soup.find_all('a'):
    l = link.get('href')
    match = re.search("\/v-appartement-condo\/ville-de-montreal\/.*\/\d+$", str(l))
    if(match):
        LINKS.append("https://www.kijiji.ca" + l)

LINKS = list(dict.fromkeys(LINKS))

APTS = []
i = 0
for i in range(0, 10):
    apt = requests.get(LINKS[i])
    apt_doc = apt.content

    apt_soup = BeautifulSoup(apt_doc, 'html.parser')
    latitude = apt_soup.find("meta",  property="og:latitude")
    longitude = apt_soup.find("meta",  property="og:longitude")
    price = re.search("'price', value: '(\d{3,4})'", str(apt_soup))
    apartment = {
                "name"  : apt_soup.title.text,
                "price" : int(price.group(1)) if price else 0,
                "url"   : LINKS[i],
                "coords" : [float(latitude['content']), float(longitude['content'])]
                }
    APTS.append(apartment)

for apt in APTS:
    print(apt)