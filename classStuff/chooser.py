import random
c = input("Do you wish to use the names of the people in your class? (Yes or No)  ")
if c.lower() == "no":
    listOfChoices = []
    while True:    
        while True:
            x = input("Please enter a choice. Enter x to exit.  ")
            if x == "x":
                break
        if len(listOfChoices) > 1:
            break
        else:
            print("You must enter more than 1 choice.")
            listOfChoices.clear()
else:
    import classmatelist
    listOfChoices = classmatelist.classmatesList
order = []
for a in range(len(listOfChoices)):
    w = random.choice(listOfChoices)
    order.append(w)
    listOfChoices.remove(w)
print(f"Your order is: ", end = "")
for b in range(len(order)):
    print(order[b], end = " ")
print("")