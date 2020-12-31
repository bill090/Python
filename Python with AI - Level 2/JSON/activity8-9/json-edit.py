import json
file = "Python/Python with AI - Level 2/JSON/activity8-9/customers.json"
f = open(file)
text = f.read()
customers = json.loads(text)
f.close()
for customer in customers:
    if customer["name"] == "John":
        customer["age"] = 31
        break
f = open(file, "w")
f.write(json.dumps(customers, indent = 4))
f.close()