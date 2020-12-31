import os
class bankAccount:
    def __init__(self, name, accountNumber, balance):
        self.name = name
        self.accountNumber = accountNumber
        self.balance = balance
    def deposit(self):
        while True:
            depositSize = input("How much would you like to deposit?  ")
            sure = input(f"Are you sure you want to deposit {depositSize}?(y/n)  ")
            while True:
                if sure.lower() == "y" or sure.lower() == "n":
                    break
                else:
                    sure = input(f"Are you sure you want to deposit {depositSize}? Enter y for yes, or n for no.  ")
                    continue
            if sure.lower() == "y":
                break
            else:
                continue
        self.balance += int(depositSize)
    def withdrawal(self):
        while True:
            withdrawalSize = input("How much would you like to withdraw?  ")
            sure = input(f"Are you sure you want to withdraw {withdrawalSize}?(y/n)  ")
            if int(withdrawalSize) > int(self.balance):
                print("You do not have enought money.")
                break
            while True:
                if sure.lower() == "y" or sure.lower() == "n":
                    break
                else:
                    sure = input(f"Are you sure you want to withdraw {withdrawalSize}? Enter y for yes, or n for no.  ")
                    continue
            if sure.lower() == "y":
                break
            else:
                continue
        self.balance = int(self.balance) - int(withdrawalSize)
    def bankFees(self):
        while True:
            sure = input("Are you sure you want to pay the bank fees?(y/n)  ")
            if sure.lower() == "y":
                break
            if sure.lower() == "y":
                break
        if sure.lower() == "y":
            self.balance = self.balance - (int(self.balance) / (5/100))
    def display(self):
        print(f"Your username is {self.name}. Your account number is {self.accountNumber}. Your balance is {self.balance}.")
def main():
    if os.path.exists("Python with AI - Level 2/OOP/files/bankStuff"):
        ID = open("Python with AI - Level 2/OOP/files/bankStuff")
        IDitems = []
        for aline in ID:
            IDitems.append(aline.split()[0])
        you = bankAccount(IDitems[0], IDitems[1], IDitems[2])
        ID.close()
    else:
        ID = open("Python with AI - Level 2/OOP/files/bankStuff", "a")
        acname = input("What is your name?  ")
        acnum = input("What is will be account number?  ")
        acbal = input("What is you balance?  ")
        ID.write(f"{acname}\n{acnum}\n{acbal}")
        ID.close()
        you = bankAccount(acname, acnum, int(acbal))
    while True:
        choice = input("Choose a function to do. D to display your information, De to deposit money, W to withdraw money, and E to exit.")
        if choice.lower() == 'd':
            you.display()
        if choice.lower() == "de":
            you.deposit()
        if choice.lower() == "w":
            you.withdrawal()
        if choice.lower() == "e":
            break
        else:
            continue
    ID = open("Python with AI - Level 2/OOP/files/bankStuff", "a")
    ID.write(f"\r{you.balance}")
main()