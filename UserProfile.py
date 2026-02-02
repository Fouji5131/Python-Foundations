name = str(input("Whats your Name: "))
age = int(input("Whats your Age: "))
hieght = float(input("Whats your Hieght in meter: "))
weight = int(input("Whats your Weight in kg: "))
category = ""


BMI = (weight / (hieght * hieght))

if BMI < 18.5:
    category = "Underweight"
elif 18.5 <= BMI < 24.9:
    category = "Normal"
elif 24.9 <= BMI < 29.9:
    category = "Overweight"
else:
    category = "Obese"

print(f"""----- USER PROFILE -----
Name   : {name}
Age    : {age}
BMI   : {BMI:.2f}
Category   : {category}
------------------------""")