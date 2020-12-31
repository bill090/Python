import turtle
import pandas as pd
def corona():
  countries = []
  list_of_colors = ["#77FF65", "orange", "yellow", "green", "blue", "purple", "red", "#346634", "#FFFFFF", "#AABB66", "#8877FF"]
  covid19 = pd.ExcelFile('/home/bill/Python/project/covid19.xlsx')
  df = pd.read_excel(covid19, 'Worksheet')

  while "end" not in countries:
    country = input("What is the name of a country you want to search (Type \"end\" to continue)  ")
    countries.append(country)
  countries.remove("end")
  my_screen = turtle.Screen()
  my_screen.setup(2160, 1000)
  my_screen.bgcolor("black")
  turtle1 = turtle.Turtle()
  for z in range(len(countries)):
    print(f"Country {z + 1} is {countries[z]} will be color {list_of_colors[z]}")

  for y in range(len(countries)):
    turtle1.penup()
    turtle1.goto(-1080, -300)
    turtle1.pendown()
    turtle1.color(list_of_colors[y])
    for a in range(2922):
      if df.lookup([a], ["prname"]) == countries[y]:
        x = turtle1.xcor()
        y2 = turtle1.ycor()
        if df.lookup([a], ["prname"]) == "NaN":
          turtle1.goto(x + 7, y2)
        elif df.lookup([a], ["numconf"]) < 100:
          turtle1.goto(x + 7, y2)
        else:
          turtle1.goto(x + 7, (int(df.lookup([a], ["numconf"])) / 100) - 300)
    x = turtle1.xcor()
    y2 = turtle1.ycor()
    turtle1.write(f"{countries[y]}", font = ("Arial", 10, "bold"))