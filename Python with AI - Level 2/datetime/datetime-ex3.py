import datetime
now = datetime.datetime.now()
duration = datetime.timedelta(seconds = 5)
new = now + duration
print("The current time is:", now.strftime("%I:&N:%S"))
print("The new time is:", new.strftime("%I:%M:%S"))
