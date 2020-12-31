import datetime
display = """-----------------------------------------------------
Please select an delivery option, or end your session
r for Regular: 4 days, Free
e for Express: 2 days, $9.99
end to end your session
-----------------------------------------------------  """
deliverSchedule = {
    "r" : [4, "Free"], 
    "e" : [2, "$9.99"]
}
times = 0
while True:
    times += 1
    deliveryMethod = input(display).lower()
    if deliveryMethod == "end":
        break
    now = datetime.datetime.now()
    estimatedDeliveryDate = now + datetime.timedelta(days = deliverSchedule[deliveryMethod][0])
    returnWindow = estimatedDeliveryDate + datetime.timedelta(days = 30)
    print(f"Your order #{times} has been placed at {now.strftime('%b %d, %Y %I:%M%p')} for {deliverSchedule[deliveryMethod][1]}")
    print(f"The estimated delivery date is {estimatedDeliveryDate.strftime('%b %d, %Y')}")
    print(f"The return window will close at {returnWindow.strftime('%b %f, %Y')}")
print("Thank you for ordering!")