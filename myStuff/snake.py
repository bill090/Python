import turtle
import time
import random

win = turtle.Screen()
win.title("Python with AI Level 1 - Snake")
win.setup(width=600,height=600)

head = turtle.Turtle()
head.speed(0)
head.shape("square")
head.color("gray")
head.penup()
head.goto(0, 100)
head.direction = "stop"

apples = []
orgiapple = turtle.Turtle()
orgiapple.speed(0)
orgiapple.shape("circle")
orgiapple.color("red")
orgiapple.penup()
orgiapple.goto(0, -100)
apples.append(orgiapple)

deathCounter = 0

high = 10
def go_up():
    if head.direction != "down":
        head.direction = "up"
 
def go_down():
    if head.direction != "up":
        head.direction = "down"
 
def go_right():
    if head.direction != "left":
        head.direction = "right"
 
def go_left():
    if head.direction != "right":
        head.direction = "left"
 
def stop():
    head.direction = "stop"
def scores(score, highscore):
    pen.clear()
    pen.write("Score: {} Highscore: {}".format(score, highscore), align = "center", font =("Courier", 24, "normal"))
pen = turtle.Turtle()
pen.speed(0)
pen.shape("square")
pen.color("white")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.pendown()
score = 0
highscore = 0
scores(score, highscore) 

win.listen()
win.onkey(go_up, "w")
win.onkey(go_down, "s")
win.onkey(go_right, "d")
win.onkey(go_left, "a")
win.bgcolor("blue")
def move():
    x = head.xcor()
    y = head.ycor()
    if head.direction == "up":
        head.sety(y + 20)
 
    if head.direction == "down":
        head.sety(y - 20)
 
    if head.direction == "right":
        head.setx(x + 20)
    if head.direction == "left":
        head.setx(x - 20)
def death():
    head.color("red")
    for p in parts:
        p.speed(100000000000000000000000000000000000000000000000000)
        p.color("red")
        p.goto(1000,1000)
        p.clear()
    parts.clear()
    head.goto(0, 100)
    head.color("gray")
    head.direction = "stop"
    for asdff in apples:
        if asdff != orgiapple:
            asdff.speed(100000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000)
            asdff.goto(1000, 1000)
            apples.remove(asdff)

parts = []
scores(0, highscore)
while True:
    win.update()
    for a in apples:
        if head.distance(a) <= 15:
            y = random.randint(-290, 290)
            while y == 0:
                y = random.randint(-290, 290)
            x = random.randint(-290, 290)
            while x == 0:
                x = random.randint(-290, 290)
            a.goto(x, y)
            new_part = turtle.Turtle()
            new_part.shape("square")
            new_part.color("gray")
            new_part.penup()    
            parts.append(new_part)
            score = score + 10
            if score > highscore:
                highscore = score
            scores(score, highscore)
    for i in range((len(parts) - 1), 0, -1):
        x = parts[i - 1].xcor()
        y = parts[i - 1].ycor()
        parts[i].goto(x, y)
    if len(parts) > 0 :
        x = head.xcor()
        y = head.ycor()
        parts[0].goto(x, y)
    if head.ycor() < -290 or head.ycor() > 290 or head.xcor() > 290 or head.xcor() < -290:
        death()
        score = 0
        scores(0, highscore)
    for b in range((len(parts) - 1), 1, -1):
        if parts[b].distance(head) < 20:
            death()
            score = 0
            scores(0, highscore)
            break
    if score > high:
        high = high * 5
        apple = turtle.Turtle()
        apple.speed(0)
        apple.shape("circle")
        apple.color("red")
        apple.penup()
        apple.goto(0, -100)
        apples.append(apple)
    move()
    time.sleep(0.05)