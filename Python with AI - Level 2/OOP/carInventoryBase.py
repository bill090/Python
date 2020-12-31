class Car:
    def __init__(self, maker, model, year, color, VIN):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color
        self.VIN = VIN
    def display(self):
        print(f"{self.maker} {self.model} {self.year} {self.color} {self.VIN}")
def main():
    cars = []
    for car in cars:
        car.display()
main()