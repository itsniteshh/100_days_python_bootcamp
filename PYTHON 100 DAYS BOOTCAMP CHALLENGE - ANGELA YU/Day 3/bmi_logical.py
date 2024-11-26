height = 1.65
weight = 84

bmi = weight / (height * height)


if bmi <= 18.5:
    print("Underweight")
elif bmi <= 25:
    print("Normal weight")
else:
    print("Obese")