def addcustomer():
    customers = open("/home/bill/Documents/Python/Python with AI - Level 2/fileHandling/files/customers.txt", "a")
    name = input("Please enter the customer's first and last name  ")
    email = input("Please enter the customer's email adress  ")
    phone = input("Please enter the customer's phone number")
    customers.write(str([name, email, phone]) + "\n")
def listcustomers():
    customers = open("/home/bill/Documents/Python/Python with AI - Level 2/fileHandling/files/customers.txt", "r")
    print(customers.read())
def menu():
    while True:
        choice = input("""A or a to add customer
L or l to List customers
Q or q to exit  """)
        if choice.lower() == "a":
            addcustomer()
            continue
        elif choice.lower() == "l":
            listcustomers()
            continue
        elif choice.lower() == "q":
            break
        else:
            print("That is not a valid option.")
            continue

menu()