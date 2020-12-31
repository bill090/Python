def mergeSortMainMain(inputList):
    global mergeEndList
    mergeEndList.append(inputList)
    return mergeSortMain(inputList)
def mergeSortMain(inputList):
    global mergeEndList
    mergeEndList.append([])
    for a in range(0, len(mergeEndList[-2]) - 1, 2):
        print("a", int(len(mergeEndList[-2]) / 2) - 1)
        mergeEndList[-1].append(mergeSort(mergeEndList[-2][a], mergeEndList[-2][a + 1]))
    if len(inputList) % 2 == 1:
        mergeEndList[-1].append(mergeEndList[-2][-1])
    if len(mergeEndList[-1]) == 1:
        return mergeEndList[-1]
    x = mergeSortMain(mergeEndList[-1])
    if x != None:
        return x
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
def splitSortMainMain(inputList):
    global splitEndList
    splitEndList.append([inputList])
    return splitSortMain(inputList)
def splitSortMain(inputList):
    global splitEndList
    splitEndList.append([])
    if len(splitEndList[-2]) == 1:
        a, b = splitSort(splitEndList[-2][0])
        splitEndList[-1].append(a)
        if b != []:
            splitEndList[-1].append(b)
    else:
        for x in splitEndList[-2]:
            a, b = splitSort(x)
            splitEndList[-1].append(a)
            if b != []:
                splitEndList[-1].append(b)
    if len(splitEndList[-1]) == len(inputList):
        return splitEndList[-1]
    if splitSortMain(inputList) != None:
        return splitSortMain(inputList)
def splitSort(inputList):
    splitEndListA = []
    splitEndListB = []
    afterHalf = False
    for a in range(len(inputList)):
        if a != (len(inputList) / 2) - 1 and afterHalf:
            splitEndListB.append(inputList[a])
        elif a == int(len(inputList) / 2) - 1:
            afterHalf = True
            splitEndListA.append(inputList[a])
        else:
            splitEndListA.append(inputList[a])
    return splitEndListA, splitEndListB
splitEndList = []
mergeEndList = []
inputList = []
while True:
    choice = input("Add a number to be sorted using the divide and conquer method. Enter \"Q\" to exit.  ")
    if choice.lower() == "q":
        break
    inputList.append(float(choice))
print(mergeSortMainMain(splitSortMainMain(inputList)))