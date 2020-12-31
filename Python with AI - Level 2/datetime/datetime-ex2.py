import datetime
now = datetime.datetime.now()
print(now)
print(f"Today is:", now.strftime("%A, %B %d, %Y"))
print(f"or:", now.strftime("%a, %b %d, %Y"))
print(f"or:", now.strftime("%a, %b %d"))
print(f"or:", now.strftime("%m/%d/%y"))