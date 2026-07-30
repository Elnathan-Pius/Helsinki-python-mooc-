name = str(input("Please tell me your name:"))
if name == "Jerry":
    print("Next please!")
if name != "Jerry":
    port = input("How many portions?")
    swe = float(port) * 5.90
    print("The total cost is", swe)
    print("Next please!")     
