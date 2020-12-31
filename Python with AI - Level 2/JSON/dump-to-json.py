import json
player = {
    "name" : "Ken Belanger",
    "email" : "kbelanger@pwa.com",
    "phone" : "416-123-4567"
}
text = json.dumps(player)
print(text)