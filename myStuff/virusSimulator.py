import turtle
import random
class Infected:
    def __init__(self, infectionRate, infectionDuration, immunityChance, infectionTime):
        self.infectionRate = infectionRate
        self.infectionTime = infectionTime
        self.immunityChance = immunityChance
        self.infectionDuration = infectionDuration
infectionDuration = 10
infectionRate = 2
immunityChance = 75
infected = [Infected(infectionRate, infectionDuration, immunityChance, 0)]
Screen = turtle.Screen()
casesCount = []
Screen.setup(width = 1500, height = 1080)
pen = turtle.Turtle()
pen.penup()
pen.goto(450, -450)
pen.pendown()
pen.goto(-450, -450)
pen.goto(-450, 450)
pen.penup()
while len(infected) != 0:
    casesCount.append(len(infected))
    willBeInfected = []
    capReached = False
    for person in infected:
        if len(infected) + len(willBeInfected) <= 500 and not(capReached):
            for a in range(person.infectionRate):
                x = Infected(infectionRate, infectionDuration, immunityChance, 0)
                willBeInfected.append(x)
        else:
            capReached = True
        if person.infectionTime >= person.infectionDuration:
            infected.remove(person)
        if random.randint(1, 100) <= person.immunityChance:
            infected.remove(person)
    for b in willBeInfected:
        infected.append(b)
    print(len(infected))
xCounter = -450
pen.goto(casesCount[0], -450)
for a in casesCount:
    xCounter += len(casesCount) / 900
    pen.goto(a, xCounter)