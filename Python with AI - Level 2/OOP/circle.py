class Circle:
    def __init__(self, radius):
        self.radius = radius
        self.pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
    def getPerimeter(self):
        return 2 * self.radius * self.pi
    def getArea(self):
        return (self.radius ** 2) * self.pi
myCircle = Circle(10)
print(f"A circle with radius {myCircle.radius}")
print(f"The permimeter is {myCircle.getPerimeter()} and the area is {myCircle.getArea()}.")
myCircle = Circle(20)
print(f"A circle with radius {myCircle.radius}")
print(f"The permimeter is {myCircle.getPerimeter()} and the area is {myCircle.getArea()}.")