import random
namesInput = open("Python/Python with AI - Level 2/others/files/names.txt")
names = []
chosens = []
for a in namesInput:
    names.append(a.split()[0])
random.shuffle(names)
chosens = random.sample(names, 500)
print("The chosen people are:", end = "")
for asdf in range(len(chosens) - 1):
    print(f" {chosens[asdf]},", end = "")
print(f" and {chosens[-1]}.", end = "")