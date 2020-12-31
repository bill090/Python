# I wasn't able to fully understand the article, but I was able to create a program based on the conclusion of the article that accepts a "root" that is within a certain range from the true root.
import turtle
import time
import math

# to input the number need to be rooted and the accuracy you choose.
a = float(input("What is the number that you want to find the root of?  "))
accuracy = int(input('What is the percentage of accuracy you want?(1 - 100)(Unfortunatly, we cannot give the exact answer with this algorithm)  %'))
pen = turtle.Turtle()
def getAccuracyRange(accuracy):
    if accuracy != 100:
        accuracyRange = [float(f"0.{accuracy}"), 2 - float(f"0.{accuracy}")]
    else:
        accuracyRange = [0.999999, 1.000001]
    return accuracyRange
def makeChart(a, aligner, pen):
    chart = turtle.Screen()
    chart.setup(width = 1500, height = 1080)
    pen.penup()
    pen.goto(450, -450)
    pen.pendown()
    pen.goto(-450, -450)
    pen.goto(-450, 450)
    pen.penup()
    pen.color("green")
    pen.goto(-450, -450 + math.sqrt(a) / aligner)
    pen.pendown()
    pen.goto(450, -450 + math.sqrt(a) / aligner)
    pen.write(f"True root: {math.sqrt(a)}", font = ("Arial", 5, "bold"))
    pen.penup()
def getAligner(a):
    if a > 1:
        aligner = ((a + 1) / 2) / 900
    else:
        aligner = 1/900
    return aligner
def getCurve(accuracyRange):
    x = 1
    resultsList = []
    while True:
        resultsList.append(x)
        if not((x * x) / a > accuracyRange[0] and (x * x) / a < accuracyRange[1]):
            x = (x + a / x) / 2
        else:
            break
    return resultsList
def writeCurve(pen, aligner, resultsList):
    xCounter = -450
    pen.color("red")
    pen.goto(xCounter, -450 + resultsList[0] / aligner)
    pen.pendown()
    for b in resultsList:
        pen.goto(xCounter, -450 + (b) / aligner)
        pen.write(f"{b}", font = ("Arial", 5, "bold"))
        xCounter += 900 / len(resultsList)
makeChart(a, getAligner(a), pen)
writeCurve(pen, getAligner(a), getCurve(getAccuracyRange(accuracy)))
time.sleep(60)