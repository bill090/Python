import turtle
fibbonacciSeq = []
for n in range(50):
    if n == 0:
        f = 0
    elif n == 1:
        f = 1
    else:
        f = fibbonacciSeq[n - 1] + fibbonacciSeq[n-2]
    fibbonacciSeq.append(f)
graph = turtle.Screen()
graph.title("Phyton with AI Level2: Recursion")
pen = turtle.Turtle()
ratio = 1.61803
xAmp = 10
yAmp = 100
pen.pencolor("blue")
pen.penup()
pen.goto(-300, 0)
pen.pendown()
pen.penup()
pen.pencolor("grey")
pen.penup()
pen.goto(-300, ratio * yAmp)
pen.pendown()
pen.goto(300, ratio * yAmp)
pen.penup()
pen.goto(2 + xAmp, fibbonacciSeq[2] / fibbonacciSeq[1])
pen.pendown()
for i in range(2, len(fibbonacciSeq)):
    pen.goto(1 * xAmp, fibbonacciSeq[1] / fibbonacciSeq[i - 1] * yAmp)