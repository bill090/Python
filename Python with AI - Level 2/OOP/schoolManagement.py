class Person:
    def __init__(self, name, email):
        self.name = name
        self.email = email
    def printContact(self):
        print(f"{self.name}  {self.email}")
    def selfIntro(self):
        print(f"Hi, I am {self.name}.")
class Student(Person):
    def __init__(self, name, email, graduateDate):
        super().__init__(name, email)
        self.graduateDate = graduateDate
    def selfIntro(self):
        super().selfIntro()
        print(f"I'm from the class of {self.graduateDate}")
    def printContact(self):
        super().printContact()
class Teacher(Person):
    def __init__(self, name, email, subject):
        super().__init__(name, email)
        self.subject = subject
    def selfIntro(self):
        super().selfIntro()
        print(f"Welcome to my {self.subject} class.")
    def printContact(self):
        super().printContact()

person = Person("Peter", "peter@anywhere.com")
student = Student("Simon", "simon@anyschool.com", 2024)
teacher = Teacher("Tara", "tara@myschool.com", "Drama")

person.printContact()
teacher.printContact()
student.printContact()

print("person.selfIntro()")
person.selfIntro()
print("teacher.selfIntro()\n")
teacher.selfIntro()
print("student.selfIntro()\n")
student.selfIntro()