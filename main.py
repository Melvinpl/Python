"""
Write a program that interprets the Body Mass Index (BMI) based on a user's weight and height.

It should tell them the interpretation of their BMI based on the BMI value.

    Under 18.5 they are underweight
    Over 18.5 but below 25 they have a normal weight
    Over 25 but below 30 they are slightly overweight
    Over 30 but below 35 they are obese
    Above 35 they are clinically obese.

https://cdn.fs.teachablecdn.com/qTOp8afxSkGfU5YGYf36

"""

height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
bmi = round((weight/(height**2)))

if bmi <= 18:
    print(f"Your BMI is {bmi}, you are underweight.")
elif bmi <= 22:
    print(f"Your BMI is {bmi}, have a normal weight.")
elif bmi <= 28:
    print(f"Your BMI is {bmi}, you are slightly overweight.")
elif bmi <= 33:
    print(f"Your BMI is {bmi}, you are obese.")
elif bmi <= 40:
    print(f"Your BMI is {bmi}, you are clinically obese.")
else:
    print("Please check the numbers you have entered")