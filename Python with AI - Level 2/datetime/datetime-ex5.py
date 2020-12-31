import datetime
nationalMonth = 7
nationalDay = 1
now = datetime.datetime.now()
NationalDay = datetime.datetime(now.year, nationalMonth, nationalDay)
if now > NationalDay:
    NationalDay = datetime.datetime(now.year + 1, nationalMonth, nationalDay)
td = NationalDay - now
print(f"There are {td.days} days until the national day")