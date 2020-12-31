import datetime
now = datetime.datetime.now()
daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', "Thursday", "Friday", "Saturday", "Sunday"]
print(now)
print(f"The current year is {now.year}")
print(f"The current month is {now.month}")
print(f"The current hour is {now.hour}")
print(f"The current minute is {now.minute}")
print(f"The day of the week is {daysOfTheWeek[now.weekday()]}")
print(f"The day of the month is {now.day}")