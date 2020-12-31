import json
dataSource = open("Python/Python with AI - Level 2/JSON/files/data.json")
data = dataSource.read()
dataSource.close()
customer = json.loads(data)
print(customer["name"])
print("---Address---")
print(customer["address"]["street"])
print(customer["address"]["city"])
print("---Children---")
for child in customer["children"]:
    print(child)