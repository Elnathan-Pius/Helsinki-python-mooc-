# programming exercise: Temperature
# description: convertimg fahrenheit to celsius using if statements
F = int(input("Type in a temp:"))
if F >= 32:
    stu = ((F - 32) * 5/9)
    print(F, " degrees Fahrenheit equals", stu,"degrees Celsius")
if F < 32:
    stu = ((F - 32) * 5/9)
    print(F, " degrees Fahrenheit equals", stu,"degrees Celsius")
    print("Brr! It's cold in here!")