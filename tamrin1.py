import math

a = float(input("Please enter first number: "))
b = float(input("Please enter first number: "))

op = input()

if op == "+" :
      result = a + b


if op == "-" :
     result = a - b

if op == "*" :
     result = a * b

if op == "/" :
     if b !=0 :
        result = a / b

     else:
        result = "ERROR"

if op == "sin":
    result = (math.sin(a))

if op == "cos":
    result = (math.cos(a))

if op == "tan":
    result = (math.tan(a))

if op == "pow":
    result=(math.pow(a,2))

if op == "factorial" :
    result=(math.factorial(a))
   
print(result)