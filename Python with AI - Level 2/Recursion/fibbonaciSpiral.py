import turtle
def fibbonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibbonacci(n - 1) + (fibbonacci(n-2))
chart = turtle.Screen()
chart.title = "Python with AI - Level 2: Recursion"
pen = turtle.Turtle()
n = 0
while True:
    x = fibbonacci(n)
    pen.circle(x, 90)
    n += 1
