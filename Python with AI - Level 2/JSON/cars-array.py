import json
dataSource = open("Python/Python with AI - Level 2/JSON/files/cars-arrayData.json")
data = dataSource.read()
dataSource.close()
cars = json.loads(data)
print("Cars\n---------------")
for car in cars:
    print(car["model"])