def menu():
    display = """Please select from the menu.
A or a to add a customer,
L or l to list the customers,
or Q or q to exit."""
    select = input(display).lower()
    if select == "a":
        addCustomers()
    elif select == "l":
        listCustomers()
    elif select == "q":
        print("Session exit.")
        return
    else:
        print("Please select a valid function.")
    menu()
def addCustomers():
    print("This function is not avaliable.")
def listCustomers():
    print("This function is not avaliable.")
menu()