string = input()
counter = 0
endList = []
for a in range(len(string)):
    if not(string[a].isalpha()):
        endList.append(string[a])
    else:
        save = string[a]
        if counter % 2 == 0:
            endList.append(string[a].lower())
        else:
            endList.append(string[a].upper())
        counter += 1
for b in range(len(endList)):
    print(endList[b], end = "")
print()
