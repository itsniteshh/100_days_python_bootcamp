# program to calculate body mass index of a person

# 1st input - enter height in meter
# 2nd input - enter weight in kgs

height = float(input("Enter your height in mtr:\n"))
weight = float(input("Enter your weight in kgs:\n"))

bmi = round(weight / (height * height),2)


if bmi < 18.3:
    print(f"Your BMI is {bmi}, you are underweight")
elif bmi < 22:
    print(f"Your BMI is {bmi}, you are normal weight")
elif bmi < 28.6:
    print(f"Your BMI is {bmi}, you are slightly overweight")
elif bmi < 32.6:
    print(f"Your BMI is {bmi}, you are underweight")
else:
    print(f"Your BMI is {bmi}, you are clinically obese")