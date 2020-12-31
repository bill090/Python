import json
dataSource = open("/home/bill/Coding/Python/Python with AI - Level 2/JSON/files/json-101Data.json")
data = dataSource.read()
player = json.loads(data)
dataSource.close()
print(player["fullName"], player["height"], player["primaryNumber"], player["birthDate"])