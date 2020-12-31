class Employee:
    def __init__(self, name, hiredDate, department, employeeID):
        self.name = name
        self.hiredDate = hiredDate
        self.department = department
        self.employeeID = employeeID
    def print(self):
        print(f"{self.name}: {self.employeeID}. Hired on {self.hiredDate}. Works in {self.department} department.")
kirk = Employee("James Kirk", 2018, "Finance", 2265) 
spock = Employee("Spock", 2017, "Marketing", 2254) 
mccoy = Employee("Leonard McCoy", 2016, "HR", 2266) 
sophia = Employee("Sophia Baker", 2015, "IT", 2159) 

employees = [kirk, spock, mccoy, sophia]
for employee in employees:
    employee.print()
keyword = ""
while keyword != "Q":
    keyword = input("Search for a employee. Enter Q to quit.  ")
    for employee in employees:
        if keyword.lower() in employee.name.lower():
            employee.print()