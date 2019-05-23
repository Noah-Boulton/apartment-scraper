from craigslist import CraigslistHousing
import requests
from bs4 import BeautifulSoup
import json

cl_h = CraigslistHousing(site='montreal', category='apa',
                         filters={'max_price': 1100})

# for apt in cl_h.get_results(limit=3):
#     print(apt)

# BOXES = {
#     "plateau1" : [
#         [45.519268, -73.586533],
#         [45.526061, -73.572195],
#         ],
#     "plateau2" : [
#         [45.513111, -73.584212],
#         [45.519905, -73.569874]
#     ],
#     "plateau3" : [
#         [45.518515, -73.580864],
#         [45.52988, -73.56466]
#     ]
# }

# box = [[45.519268, -73.586533], [45.526061, -73.572195]]

APTS = []
for result in cl_h.get_results(limit=15):
    apt = requests.get(result['url'])
    apt_doc = apt.content

    apt_soup = BeautifulSoup(apt_doc, 'html.parser')
    geo = apt_soup.find(class_="viewposting")

    apartment = {
                "name"  : result['name'],
                "price" : result['price'],
                "url"   : result['url'],
                "coords" : [float(geo['data-latitude']), float(geo['data-longitude'])]
                }
    APTS.append(apartment)
    print(apartment)

# for apt in APTS:
#     coords = apt['coords']
#     for box in BOXES:
#         if box[0][0] < coords[0] < box[1][0] and box[1][1] < coords[1] < box[0][1]:
#             print("IN THE PLATEAU")


