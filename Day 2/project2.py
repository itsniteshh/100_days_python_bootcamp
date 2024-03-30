# a program to calculate tip and total payment

print("Welcome to the tip calculator program!")
total_bill = int(input("what was the total bill?\n"))

#tip %
tip = int(input("How much tip would you like to give? 10, 12 or 15?\n"))/100

# no of person
total_person = int(input("how many people to split the bill?\n"))

#calculations

final_bill = (total_bill + (total_bill * tip)) / total_person
print(f"Each person should pay: rupees {round(final_bill)}")