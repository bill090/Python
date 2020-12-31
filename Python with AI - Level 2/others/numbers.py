inputNumbers = []
listOfDefects = []
x = open("Python with AI - Level 2/fileHandling/files/dpaIn.txt", "r")
for aline in x:
    if aline.split()[0].isdecimal():
        inputNumbers.append(int(aline.split()[0]))
x.close()
y = open("Python with AI - Level 2/fileHandling/files/dpaOut.txt", "a")
print(inputNumbers, len(inputNumbers))
for a in range(len(inputNumbers)):
    listOfDivisors = []
    for b in range(1, inputNumbers[a]):
        if inputNumbers[a] % b == 0:
            listOfDivisors.append(b)    
    c = 0
    for d in range(len(listOfDivisors)):
        c += listOfDivisors[d]    
    if c > inputNumbers[a]:
        y.write(f"{inputNumbers[a]} is a deficient number.\n")
        continue
    if c < inputNumbers[a]:
        y.write(f"{inputNumbers[a]} is a abundant number.\n")
        continue
    else:
        y.write(f"{inputNumbers[a]} is a perfect number.\n")
        continue
y.close()