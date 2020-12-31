import random
import turtle
import time
import datetime
list_of_things = ["get out", "stop spying on me", "am i 18 yet?", "OH MY GOSH JUST STOP BEING HERE NOW", "WHY ARE YOU HERE", "PLEASE LEAVE NOW", """i cannot stress this enough.
please leave.""", "LEAVE NOW OR I WILL, BUT FOREVER", "JUST LEAVE!!!", "FOR GOD'S SAKE, STOP TAKING PICTURES OF THIS SCREEN", 'JUST GET OUT', '''please leave now,
i haven't done anything wrong''']
myScreen = turtle.Screen()
myScreen.setup(width = 1920, height = 1080)
annoy = turtle.Turtle()
annoy.hideturtle()
annoy.penup()
annoy.goto(-860, 0)
annoy.pendown()
times = 0
done0 = False
done1 = False
done2 = False
done3 = False
while True:
    annoyer = random.choice(list_of_things)
    annoy.write("{}".format(annoyer), font = ("Calibri", 32, "bold"))
    time.sleep(60)
    annoy.clear()
    times += 1
    if times >= 3 and not(done0):
        list_of_things.append('''actually. if you stopped,
i could be satisfied.''')
        done0 = True
    elif times >= 10 and not(done1):
        list_of_things.append("just get out now. please leave. i cannot say this enough")
        done1 = True
        for i in range(10):
            list_of_things.append("go to https://www.youtube.com/watch?v=dQw4w9WgXcQ and leave me alone")
    elif times >= 60 and not(done2):
        list_of_things.append("""how many pictures have you taken?""")
        list_of_things.append("man, how long have you been doing this for?")
        list_of_things.append('JUST GET OUT!!!!!')
        for i in range(20):
            list_of_things.append("go to https://www.youtube.com/watch?v=dQw4w9WgXcQ and leave me alone")
        done2 = True
    elif times >= 120 and not(done3):
        list_of_things.append("""just get out already.
you won't find anything here.""")