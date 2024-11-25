
print("Welcome to the tip caculator program")


bill = int(input("What was the total bill? "))
tip = int(input("How much % tip would you like to give? "))
person = int(input("How many people to split the bill? "))

total_bill = bill + (bill * (tip/100))
per_person = total_bill / person

print(f"Each person should pay: {per_person}")