wage = float(input("Hourly wage:"))
worked = int(input("hours worked:"))
day = input("Day of the week:")
if day == "Sunday":
    TU = (wage * worked)*2
    print("Daily wages:",TU,"euros")
if day != "Sunday":
    TU = wage * worked 
    print("Daily wages:",TU,"euros")
