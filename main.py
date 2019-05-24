from craigslist import craigslist
from kijiji import kijiji
from distance import distance

metro_stations = {
                    "Verdun" : [45.459444, -73.571667],
                    "De L'Eglise" : [45.462778, -73.566944],
                    "LaSalle" : [45.470833, -73.566389],
                    "Charlevoix" : [45.478333, -73.569444],
                    "Lionel-Groulx" : [45.482778, -73.579722],
                    "Atwater" : [45.489722, -73.586111],
                    "Guy-Concordia" : [45.495, -73.58],
                    "Peel" : [45.500833, -73.574722],
                    "McGill" : [45.503889, -73.571667],
                    "Place-des-Arts" : [45.508056, -73.568611],
                    "Saint-Laurent" : [45.510833, -73.564722],
                    "Berri-UQAM" : [45.515278, -73.561111],
                    "Beaudry" : [45.518889, -73.555833],
                    "Place-Saint-Henri" : [45.477222, -73.586667],
                    "Georges-Vanier" : [45.488889, -73.576667],
                    "Lucien-L'Allier" : [45.495, -73.571111],
                    "Bonaventure" : [45.498056, -73.567222],
                    "Square-Victoria-OACI" : [45.501944, -73.563056],
                    "Place-d'Armes" : [45.506389, -73.559722],
                    "Champ-de-Mars" : [45.51, -73.556389],
                    "Sherbrooke" : [45.518889, -73.568889],
                    "Mont-Royal" : [45.524444, -73.581667],
                    "Laurier" : [45.527222, -73.586667],
                    "Rosemont" : [45.531111, -73.5975],
                    "Beaubien" : [45.535556, -73.604444],
                    "Jean-Talon" : [45.538889, -73.614167]
                }

if __name__ == "__main__":    
    print("Getting Craigslist apartments.")
    craigslist_apts = craigslist(2)

    print("Getting Kijiji apartments.")
    kijiji_apts = kijiji(2)

    APTS = craigslist_apts + kijiji_apts
    for apt in APTS:
        closest_metro = None
        shortest_distance = 1000000
        for metro in metro_stations:
            dist = distance(metro_stations[metro], apt['coords'])
            if(dist < shortest_distance):
                shortest_distance = dist
                closest_metro = metro
        apt['metro'] = closest_metro
        apt['distance'] = shortest_distance
        print(apt)
