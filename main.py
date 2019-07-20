from craigslist import get_craigslist_links, get_craigslist_listings
from kijiji import get_kijiji_links, get_kijiji_listings
from slackclient import SlackClient
import os

from settings import getAPIToken
from slack_bot import post_listing_to_slack

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker

engine = create_engine('sqlite:///listings.db', echo=False)
Base = declarative_base()
class Listing(Base):
    """
    A table to store data on craigslist listings.
    """
    __tablename__ = 'listings'
    id = Column(Integer, primary_key=True)
    link = Column(String, unique=True)
    lat = Column(Float)
    lon = Column(Float)
    name = Column(String)
    price = Column(Float)
    metro_station = Column(String)
    distance = Column(Float)

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

if __name__ == "__main__":    
    # rows = session.query(Listing).count()
    # print(rows)
    print("Getting Craigslist apartments.")
    sc = SlackClient(getAPIToken())

    craigslist_links = get_craigslist_links()
    craigslist_listings = []
    for link in craigslist_links:
        listing = session.query(Listing).filter_by(link=link).first()

        if listing is None:
            apartment = get_craigslist_listings(link)
            new_listing = Listing(
                link = link,
                lat = apartment['coords'][0],
                lon = apartment['coords'][1],
                name = apartment['name'],
                price = apartment['price'],
                metro_station = apartment['metro'],
                distance = apartment['distance']
            )
            session.add(new_listing)
            session.commit()
            craigslist_listings.append(apartment)

    print("Getting Kijiji apartments.")
    kijiji_links = get_kijiji_links()
    kijiji_listings = []
    for link in kijiji_links:
        listing = session.query(Listing).filter_by(link=link).first()

        if listing is None:
            apartment = get_kijiji_listings(link)
            new_listing = Listing(
                link = link,
                lat = apartment['coords'][0],
                lon = apartment['coords'][1],
                name = apartment['name'],
                price = apartment['price'],
                metro_station = apartment['metro'],
                distance = apartment['distance']
            )
            session.add(new_listing)
            session.commit()
            kijiji_listings.append(apartment)
    
    for apt in craigslist_listings + kijiji_listings:
        studio = False
        if 'studio' in apt['name'].lower():
            studio = True
        if '1 1/2' in apt['name'].lower():
            studio = True
        if '1 ½' in apt['name'].lower():
            studio = True
        if '1.5' in apt['name'].lower():
            studio = True
        if '1 bd' in apt['name'].lower():
            studio = True
        if '1 bed' in apt['name'].lower():
            studio = True
        if '2.5' in apt['name'].lower():
            studio = True
        if '2 bd' in apt['name'].lower():
            studio = True
        if '2 bed' in apt['name'].lower():
            studio = True
        if '2 1/2' in apt['name'].lower():
            studio = True
        if '2 ½' in apt['name'].lower():
            studio = True
        if '3.5' in apt['name'].lower():
            studio = True
        if '3 1/2' in apt['name'].lower():
            studio = True
        if '3 ½' in apt['name'].lower():
            studio = True
        if '4.5' in apt['name'].lower():
            studio = True
        if '4 1/2' in apt['name'].lower():
            studio = True
        if '4 ½' in apt['name'].lower():
            studio = True
        if(apt['distance'] < 1.2 and not studio):
            post_listing_to_slack(sc, apt)