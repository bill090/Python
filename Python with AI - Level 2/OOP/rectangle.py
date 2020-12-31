class Rectangle:
    def __init__(self, width, length):
        self.length = length
        self.width = width
    def getArea(self):
        return self.length * self.width
    def getPerimeter(self):
        return 2 * (self.width + self.length)
    def display(self):
        print(f"{self.getArea()} is the area, and {self.getPerimeter()} is the perimeter.")
myRectangle = Rectangle(10, 10)
myRectangle.display()
myRectangle = Rectangle(10, 20)
myRectangle.display()