import random
x = open("Python/Python with AI - Level 2/others/files/names.txt", "a")
people = ['WilburSoot', 'ItsFundy', 'The_Eret', 'Grian', 'GoodTimesWithScar', 'Iskall85', 'MumboJumbo', 'Renthedog', 'Dream', 'Sapnap', 'AntFrost', 'GeorgeNotFound', 'BadBoyHalo', 'Niki']
for a in range(700):
    if random.choice([True, False]) and len(people) > 0:
        choice = random.choice(people)
        x.write(f"{choice}\n")
        people.remove(choice)
    else:
        name = random.choice(["B", "C", "D", "F", "G", "H", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T", "V", "W", "X", "Z", "Y"]) + random.choice(["a", "e", "i", "o", "u"]) + random.choice(["bl", "br", "cl", "cr", "dr", "fr", "tr", "fl", "gl", "gr", "pl", "pr", "sl", 'sm', 'sp' "st"]) + random.choice(["ai", "ea", "ee", "oa", "oo", "ou"]) + random.choice(["b", "c", "d", "f", "g", "h", "j", "k", "l", "m", "n", "p", "q", "r", "s", "t", "v", "w", "x", "z", "y"]) + '\n'
        x.write(name)