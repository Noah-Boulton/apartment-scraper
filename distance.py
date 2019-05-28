import math

metro_stations = {
                    "Lionel-Groulx" : [45.482778, -73.579722],
                    "Atwater" : [45.489722, -73.586111],
                    "Guy-Concordia" : [45.495, -73.58],
                    "Peel" : [45.500833, -73.574722],
                    "McGill" : [45.503889, -73.571667],
                    "Place-des-Arts" : [45.508056, -73.568611],
                    "Saint-Laurent" : [45.510833, -73.564722],
                    "Berri-UQAM" : [45.515278, -73.561111],
                    "Beaudry" : [45.518889, -73.555833],
                    "Papineau" : [45.523611, -73.552222],
                    "Frontenac" : [45.533333, -73.551944],
                    "Prefontaine" : [45.541667, -73.554444],
                    "Villa-Maria" : [45.479444, -73.619722],
                    "Snowdon" : [45.485556, -73.628056],
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

def distance(coord1, coord2):
    lon1, lat1, lon2, lat2 = map(math.radians, [coord1[0], coord1[1], coord2[0], coord2[1]])
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.sin(dlat/2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon/2)**2
    c = 2 * math.asin(math.sqrt(a))
    km = 6367 * c
    return km

def closest_metro(coords):
    closest_metro = None
    shortest_distance = 1000000
    for metro in metro_stations:
        dist = distance(metro_stations[metro], coords)
        if(dist < shortest_distance):
            shortest_distance = dist
            closest_metro = metro
    return [closest_metro, shortest_distance]