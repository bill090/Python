class Shape:
    name = "Shape"
    def getArea(self):
        pass
    def getPerimeter(self):
        pass
    class Rectangle:
        def __init__(self, width, length):
            self.width = width
            self.length = length
        def getArea(self):
            return self.width * self.length
        def getPerimeter(self):
            return 2 * (self.width + self.length)
    class Circle:
        def __init__(self, radius):
            self.radius = radius
            self.pi = 3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679
        def getPerimeter(self):
            return 2 * self.radius * self.pi
        def getArea(self):
            return (self.radius ** 2) * self.pi
def main():
    myRectangle = Shape.Rectangle(10, 20)
    print(f"The area of myRectangle is {myRectangle.getArea()}, and its permimeter is {myRectangle.getPerimeter()}")
    myCircle = Shape.Circle(10)
    print(f"The area of myCircle is {myCircle.getArea()}, and its perimeter is {myCircle.getPerimeter()}")
main()