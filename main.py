from craigslist import craigslist
from kijiji import kijiji

if __name__ == "__main__":
    print("Getting Craigslist apartments.")
    craigslist_apts = craigslist()

    print("Getting Kijiji apartments.")
    kijiji_apts = kijiji()

    APTS = craigslist_apts + kijiji_apts
    for apt in APTS:
        print(apt)
