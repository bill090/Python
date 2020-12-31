classmates = open("/home/bill/Python/classStuff/classmates.txt", "r")
classmatesList = []
listOfSimilars = []
while True:
    d = input("Are there any classmates with identical names? (Enter a full name) (Enter \"x\" to exit)")
    if d == "x":
        break
    else:
        listOfSimilars.append(d)
for aline in classmates:
    names = aline.split()
    for e in range(len(listOfSimilars)):
        if names[0] == listOfSimilars[e]:
            classmatesList.append(names[0], names[1][0] + ".")
            break
        else:
            classmatesList.append(names[0])
            break