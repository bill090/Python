def mergeSort(inputListA, inputListB):
    endResult = []
    while True:
        if inputListA == []:
            for a in inputListB:
                endResult.append(a)
            break
        if inputListB == []:
            for a in inputListA:
                endResult.append(a)
            break
        if inputListA[0] >= inputListB[0]:
            endResult.append(inputListB[0])
            inputListB.pop(0)
            continue
        if inputListA[0] < inputListB[0]:
            endResult.append(inputListA[0])
            inputListA.pop(0)
            continue
    return endResult
def splitSort(inputList):
    endList = []
    for a in inputList:
        endList.append([a])
    return endList
def mainSort(inputList):
    x = splitSort(inputList)
    endResults = [x]
    while True:
        endResults.append([])
        if len(endResults[-2]) == 1:
            break
        for a in range(0, len(endResults[-2]) - 1, 2):
            endResults[-1].append(mergeSort(endResults[-2][a], endResults[-2][a + 1]))
        if len(endResults[-2]) % 2 == 1:
            endResults[-1].append(endResults[-2][-1])
    return endResults[-2]
inputList = []
while True:
    choice = input("Add a number to be sorted using the divide and conquer method. Enter \"Q\" to exit.  ")
    if choice.lower() == "q":
        break
    inputList.append(float(choice))
print(mainSort(inputList))