leafsplayers = open("Python with AI - Level 2/fileHandling/files/leafsplayers.txt", "r")
print("Leafs all time players")
for aline in leafsplayers:
    values = aline.split()
    print(values[0], values[1], values[2], values[3])
leafsplayers.close()