class Car:
    def __init__(self, maker, model, year, color, VIN):
        self.maker = maker
        self.model = model
        self.year = year
        self.color = color
        self.VIN = VIN
    def display(self):
        print(f"The maker of this car is {self.maker}. Its model is the {self.model}, and was made in the year {self.year}. It's the color {self.color}. Its VIN is {self.VIN}")
def main():
    cars = [Car("Acura", "ILX", 2018, "blue", "1P4GP45R4TB273312"), Car("Acura", "TLX", 2020, "gray", "1FMCU9G95DUD83616"), Car("Alfa Romeo", "Giulia", 1962, "blue", "5UXFE83599L186746"), Car("Alfa Romeo", "MiTo Quadrifoglio Verde", 2009, "gray", "1GKEV33748J137440"), Car("Alpine", "A110", 1962, "blue", "5XXGN4A71EG348964"), Car("Alpine", "A110S", 2019, "gray", "4F4CR12A4VTM74870"), Car("Ariel", "Nomad", 2015, "orange", "KNAFZ6A30E5250146"), Car("Ariel", "Atom", 1999, "yellow", "1FDKF37G0VEB57657"), Car("Aro", "M Series", 1963, "gray", "2CKDL63FX76284694"), Car("Aro", "24 Series", 1991, "blue", "2CKDL63FX76284694")]
    for car in cars:
        car.display()
main()