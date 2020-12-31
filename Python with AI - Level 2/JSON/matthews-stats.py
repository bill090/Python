import json
dataSource = open("Python/Python with AI - Level 2/JSON/files/austonMatthews.json")
data = dataSource.read()
matthewsStats = json.loads(data)
dataSource.close()
print(f"Player name: {matthewsStats['person']['fullName']}")
print(matthewsStats["person"]['primaryNumber'], matthewsStats["person"]['height'], matthewsStats["person"]["primaryPosition"]["name"])