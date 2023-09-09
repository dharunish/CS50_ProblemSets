expression = input("Expression: ")
expression = expression.split(" ")
x = float(expression[0])
y = expression[1]
z = float(expression[2])

if y == "+":
    print(x+z)
elif y == "-":
    print(x-z)
elif y == "/":
    if z == 0:
        print("cannot divide by 0")
    else:
        print(x/z)
elif y == "*":
    print(x*z)

