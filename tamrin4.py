name = input("Name :")

family = input("Last Name :")

a = int(input("NUM1:"))

b = int(input("NUM2:"))

c = int(input("NUM3 :"))

average = ((a + b + c)/3)

if average >= 17 :
    result = "Great"

if average >= 12 and average <= 17 :
    result = "Great"

if average < 12 :
    result = "Fail"

print(result)