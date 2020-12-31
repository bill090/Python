import datetime
today = datetime.date.today()
day = datetime.timedelta(days = 1)
yesterday = today - day
tomorrow = today + day
print(f"""Today is {today}.
Tomorrow is {tomorrow}.
Yesterday was {yesterday}.""")