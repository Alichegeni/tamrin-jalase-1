a = int (input("Weight in Kilograms :"))

b = int (input("Height in metres :"))

BMI = float (a /b)


if BMI < 18.5 :
    result = "UNDERWEIGHT"

if BMI > 18.5 and BMI < 24.9 :
    result="NORMAL"


if BMI > 30 and BMI < 34.9 :
    result="OBESE"

if BMI > 35 :
    result = "EXTREMELY OBESE"

print(result)