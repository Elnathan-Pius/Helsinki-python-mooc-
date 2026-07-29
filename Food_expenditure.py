times = int(input("How many times a week do you eat at the student cafeteria?"))
pri = float(input("The price of a typical student lunch?"))
mon = float(input("How much money do you spend on groceries in a week?"))

stuff = (times * pri) + mon
stuff2 = stuff / 7
stuff1 = (times * pri) + mon
print("Average food expenditure:")
print("Daily:", stuff2, "euros")
print("Weekly:", stuff1, "euros")