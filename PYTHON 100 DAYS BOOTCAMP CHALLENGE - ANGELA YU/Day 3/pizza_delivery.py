print("Welcome to the pizza delivery program")

size = input("what size pizza do you want? S, M or L: ").lower()
pepporani = input("Do you want additional pepporani on your pizza? Y or N: ").lower()
extra_cheese = input("Do you want extra cheese? Y or N: ").lower()

total_amount = 0

if size == "s":
    total_amount += 100
    
    if pepporani == "y":
        total_amount += 15
    
    if extra_cheese == "Y":
        total_amount += 10
        
elif size == "m":
    total_amount += 150
    
    if pepporani == "y":
        total_amount += 20
    
    if extra_cheese == "Y":
        total_amount += 10

else:
    total_amount += 200
    
    if pepporani == "y":
        total_amount += 20
    
    if extra_cheese == "Y":
        total_amount += 10
        
print(f"Here is your total bill {total_amount}")