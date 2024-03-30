# program to calculate body mass index of a person

# 1st input - enter height in meter
# 2nd input - enter weight in kgs

height = float(input("Enter your height in mtr:\n"))
weight = float(input("Enter your weight in kgs:\n"))

bmi = weight / (height * height)
print(f"Your Body Mass Index is {round(bmi, 2)}")