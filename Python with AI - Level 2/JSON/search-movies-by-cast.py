import json
file = "Python/Python with AI - Level 2/JSON/files/movies.json"
f = open(file)
movies_text = f.read()
f.close()
movies = json.loads(movies_text)
cast = []
print('''----------------------------------------------------------------------
Please enter a cast member to search for. Enter "X" to stop searching.
----------------------------------------------------------------------''')
while True:
    print("Input:  ", end = "")
    choose = input()
    print()
    if choose != "X":
        cast.append(choose)
    else:
        break
withCast = []
for movie in movies:
    count = 0
    for a in cast:
        if a in movie["cast"]:
            count += 1
    if count == len(cast):
        withCast.append(movie["title"])
print('''--------------------------------------
These are some movies with that cast:''')
for b in withCast:
    if b != withCast[-1]:
        print(f"\"{b}\",")
    else:
        print(f"and \"{b}\".")