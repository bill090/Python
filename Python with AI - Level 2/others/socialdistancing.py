import os
fileNum = input("Which file number would you like to acsess?  ")
inputFile = open(f"Python/Python with AI - Level 2/others/Social Distancing InOut Data File/{fileNum}.in")
lineCount = 0
endDistances = [0]
endDistance = 0
for aline in inputFile:
    lineCount += 1
    if lineCount == 2:
        inputNum = aline 
inputFile.close()
outputNum = ""
distances = [0]
for a in range(len(inputNum) - 1):
    if inputNum[a] == "0":
        if a == 0:
            firstZero = True
        distances[-1] += 1
    if inputNum[a] == "1":
        if a == 0:
            firstZero = False
        else:
            distances.append(0)
highHigh = 0
for a in distances:
    if a > highHigh:
        highHigh = a
smallHigh = 0
highHighTwice = False
for a in distances:
    if a > smallHigh and (a != highHigh or highHighTwice):
        smallHigh = a
    if a == highHigh:
        highHighTwice = True
highUsed = False
smallUsed = False
distanceNum = -1
distancePart = 0
for a in inputNum:
    if distanceNum == len(distances) and distancePart == distances[-1]:
        break
    if a == "1":
        distanceNum += 1
        distancePart = 0
        outputNum = "{}1".format(outputNum)
    elif a == "0":
        distancePart += 1
        if not firstZero and (distances[distanceNum] == highHigh or (distances[distanceNum] == smallHigh)) and distancePart == int(distances[distanceNum] / 2) + 1:
            outputNum = "{}1".format(outputNum)
        else:
            outputNum = "{}0".format(outputNum)
for a in range(len(inputNum) - 1):
    if outputNum[a] == "0":
        endDistances[-1] += 1
    if outputNum[a] == "1":
        endDistances.append(0)
for a in endDistances:
    if a > endDistance:
        endDistance = a
os.remove(f"Python/Python with AI - Level 2/others/Social Distancing InOut Data File/{fileNum}.out")
outputFile = open(f"Python/Python with AI - Level 2/others/Social Distancing InOut Data File/{fileNum}.out", "w")
outputFile.write(str(endDistance))