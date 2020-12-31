class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def bark(self):
        print(f"{self.name} is barking woof woof...")
    def move(self):
        print(f"{self.name} is moving...")
bobby = Dog("bobby", 3)
bobby.move()
bobby.bark()
semi = Dog("semi", 2)
semi.move()
semi.bark()