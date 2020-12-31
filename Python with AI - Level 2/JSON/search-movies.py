import json
file = "Python/Python with AI - Level 2/JSON/files/movies.json"
f = open(file)
movies_text = f.read()
f.close()
movies = json.loads(movies_text)
genre = input('''----------------------------------
Please enter a genre to search for
----------------------------------
Input:  ''')
withGenre = []
for movie in movies:
    for a in movie["genres"]:
        if a.upper() == genre.upper():
            withGenre.append(movie["title"])
print('''--------------------------------------
These are some movies with that genre:''')
for b in withGenre:
    if b != withGenre[-1]:
        print(f"\"{b}\",")
    else:
        print(f"and \"{b}\".")