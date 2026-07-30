num1 = int(input("Number 1:")) 
num2 = int(input("Number 2:"))
oper = input("operation:")
if oper == "add":
    tu = num1 + num2
    print(num1,"+",num2, "=",tu)
if oper == "multiply":
    tu = num1 * num2
    print(num1,"*",num2, "=",tu)
if oper == "subtract":
    tu = num1 - num2
    print(num1,"-",num2, "=",tu)