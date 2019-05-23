import requests 

result = requests.get("https://montreal.craigslist.org/search/apa?lang=en&cc=us")
html_doc = result.content

from bs4 import BeautifulSoup
import re 
soup = BeautifulSoup(html_doc, 'html.parser')

LINKS = []
for link in soup.find_all('a'):
    l = link.get('href')
    match = re.search("^https://montreal.craigslist.org/apa/d/",l)
    if(match):
        LINKS.append(l)

LINKS = list(dict.fromkeys(LINKS))

APTS = []
for i in range(0,10):
    print("Getting link ", i)
    apt = requests.get(LINKS[i])
    apt_doc = apt.content
    apt_soup = BeautifulSoup(apt_doc, 'html.parser')
    price = apt_soup.find(class_="price")
    geo = apt_soup.find(class_="viewposting")
    apartment = {
                "name"  : apt_soup.title.text,
                "price" : int(price.text[1:]),
                "url"   : LINKS[i],
                "coords" : [float(geo['data-latitude']), float(geo['data-longitude'])]
                }
    APTS.append(apartment)

box =  [[45.501865,-73.583595],
        [45.513233,-73.56739]]

# filter by price 
for apt in APTS:
        print(apt)
#     if(apt['price'] < 1100):
#         coords = apt['coords']
#         if box[0][0] < coords[0] < box[1][0] and box[0][1] < coords[1] < box[1][1]:
#             print(apt)
