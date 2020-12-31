import json
def menu():
    display = '''    ***************************************
                Contacts Book
    ***************************************
    Please select a function from the menu.
    ***************************************
        Enter E or e to edit a contact,
        S or s to search the contacts,
        L or l to display all contacts,
            or Q or q to exit.
    ***************************************
    '''
    while True:
        choice = input(display)
        if choice.lower() == "e":
            editMenu()
        elif choice.lower() == "s":
            searchContacts()
        elif choice.lower() == "l":
            displayContacts()
        elif choice.lower() == "q":
            break
        else:
            print("Use a valid option.")
def searchContacts():
    choice = input("What person do you want to search for?  ")
    file = "/home/bill/Coding/Python/Python with AI - Level 2/JSON/project/contacts.json"
    f = open(file)
    text = f.read()
    contacts = json.loads(text)
    f.close()
    for contact in contacts:
        if contact["name"] == choice:
            print(f"{contact['name']}. Email: {contact['email']}. Phone Number: {contact['phoneNumber']}.")
def displayContacts():
    file = "/home/bill/Coding/Python/Python with AI - Level 2/JSON/project/contacts.json"
    f = open(file)
    text = f.read()
    contacts = json.loads(text)
    f.close()
    for contact in contacts:
        print(f"{contact['name']}. Email: {contact['email']}. Phone Number: {contact['phoneNumber']}.")
def editMenu():
    editDisplay = '''    *******************************************
                Contacts Book
    *******************************************
    Please select a function from the menu.
    *******************************************
    Enter E or e to change contact information,
           A or a to add a contact,
          D or d to delete a contact,
      or Q or q to go back to the main menu.
    *******************************************
    '''
    while True:
        choice = input(editDisplay)
        if choice.lower() == "e":
            choice = input("Which contact would you like to find?  ")
            editContact(choice)
        elif choice.lower() == "a":
            choice = input("Who do you want to add?  ")
            addContact(choice)
        elif choice.lower() == "d":
            choice = input("Whose contact do you want to delete?  ")
            deleteContact(choice)
        elif choice.lower() == "q":
            break
        else:
            print("Use a valid option.")
def editContact(contact):
    file = "/home/bill/Coding/Python/Python with AI - Level 2/JSON/project/contacts.json"
    f = open(file)
    text = f.read()
    contacts = json.loads(text)
    f.close()
    for person in contacts:
        if person["name"] == contact:
            person["age"] = input("What is this person's current age?  ")
            person["phoneNumber"] = input("What is this person's current phone number?  ")
            person["email"] = input("What is this person's current email?  ")
            break
    f = open(file, "w")
    f.write(json.dumps(contacts, indent = 4))
    f.close()
def addContact(person):
    file = "/home/bill/Coding/Python/Python with AI - Level 2/JSON/project/contacts.json"
    f = open(file, "r")
    text = f.read()
    contacts = json.loads(text)
    f.close()
    contact = {
        "name" : person,
        "age" : input(f"How old is {person}?  "),
        "phoneNumber" : input(f"What is {person}'s phone number?  "),
        "email" : input(f"What is {person}'s email?  ")
    }
    contacts.append(contact)
    f = open(file, "w")
    f.write(json.dumps(contacts, indent = 4))
    f.close()
def deleteContact(person):
    file = "/home/bill/Coding/Python/Python with AI - Level 2/JSON/project/contacts.json"
    f = open(file, "r")
    text = f.read()
    contacts = json.loads(text)
    f.close()
    for contact in contacts:
        if contact["name"] == person:
            contacts.remove(contact)
            break
    f = open(file, "w")
    f.write(json.dumps(contacts, indent = 4))
    f.close()
menu()