# module

#calcuate distance between two points 
from math import sin, cos, sqrt, atan2, radians

def calculate_distance(point1, point2):
    # approximate radius of earth in km
    R = 6373.0
    lat1 = radians(point1[0])
    lon1 = radians(point1[1])
    lat2 = radians(point2[0])
    lon2 = radians(point2[1])

    dlon = lon2 - lon1
    dlat = lat2 - lat1

    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = R * c
    return distance

#Sample 
lat1 = 43.7623948471533
lon1 = -79.3640709503166
lat2 = 43.6822930225308
lon2 = -79.32099455186122

distance = calculate_distance((lat1,lon1),(lat2,lon2))
print("Result:", distance)
print("Should be:", 9.5, "km")