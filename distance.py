import math

metro_stations = {
                    "Finch" : [43.780556, -79.414722],
                    "North York Centre" : [43.768333, -79.412778],
                    "Sheppard–Yonge" : [43.761389, -79.410833],
                    "York Mills" : [43.744167, -79.406667],
                    "Lawrence" : [43.725, -79.402222],
                    "Eglinton" : [43.705833, -79.398333],
                    "Davisville" : [43.697778, -79.397222],
                    "St. Clair" : [43.687778, -79.393056],
                    "Summerhill" : [43.682222, -79.390833],
                    "North Toronto" : [43.680833, -79.390556],
                    "Rosedale" : [43.676944, -79.388889],
                    "Bay" : [43.670278, -79.39],
                    "Bloor–Yonge" : [43.671111, -79.385833],
                    "Wellesley" : [43.665278, -79.383889],
                    "College" : [43.661389, -79.383056],
                    "Dundas" : [43.656389, -79.380833],
                    "Queen" : [43.6525, -79.379167],
                    "King" : [43.649167, -79.377778],
                    "Union" : [43.645556, -79.380556]
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