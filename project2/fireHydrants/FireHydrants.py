import json, datetime
from math import sin, cos, sqrt, atan2, radians, inf
distances = []
point1 = [int(input("What is your latitude?  ")), int(input("What is your longitude?  "))]
start = datetime.datetime.now()
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
fireHydrantsList = open("project2/fireHydrants/Fire Hydrants Data.json", "r")
fireHydrantsUTF8BOM = fireHydrantsList.read()
fireHydrants = json.loads(fireHydrantsUTF8BOM)
fireHydrantsList.close()
print(len(fireHydrants["features"]))
for fireHydrant in fireHydrants["features"]:
    distances.append({"distance" : calculate_distance(point1, fireHydrant["geometry"]["coordinates"]), "place" : fireHydrant["properties"]["ADDR_QUAL"]})
top10 = []
for b in range(0, 10):
    xth = {"distance" : inf}
    for a in distances:
        if a["distance"] < xth["distance"]:
            xth = a
    distances.remove(xth)
    top10.append(xth)
counter = 0
xthNumsList = ["10th", "9th", "8th", "7th", "6th", "5th", "4th", "3rd", "2nd", "1st"]
for a in top10:
    print(f"The {xthNumsList[counter]} closest fire hydrant is {a['distance']} away from you, at {a['place']}.")
end = datetime.datetime.now()
duration = end - start
print(f"Your query took {duration} to complete.")