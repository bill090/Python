x = open(input("Please enter the file path of the file you want to acsess.  "), "a")
while True:
    y = input("Enter the text you want to insert. To make a new line press Enter. To end, enter \"x\".  ")
    if y == "x":
        break
    if y == "":
        x.write("\n")
    else:
        x.write(y)
x.close()