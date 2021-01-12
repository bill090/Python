import json
fireHydrantsList = open("project2/Fire Hydrants Data.json")
fireHydrants = fireHydrantsList.read()
fireHydrantsDictionary = json.loads(fireHydrants)
fireHydrantsList.close()