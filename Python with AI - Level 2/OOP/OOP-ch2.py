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
class Parallelipid(Rectangle):
    def __init__(self, width, length, height):
        super().__init__(length, width)
        self.height = height
    def getArea(self):
        return 2 * (self.width * self.length + self.length * self.height + self.width * self.height)
    def getPerimeter(self):
        return 3 * (self.width + self.length + self.height)
    def getVolume(self):
        return self.width * self.length * self.height
myParallelipid = Parallelipid(10, 10, 10)
print(f'The surface area of myParallelipid is {myParallelipid.getArea()}, its volume is {myParallelipid.getVolume()}, and its perimeter (total line length) is {myParallelipid.getPerimeter()}.')