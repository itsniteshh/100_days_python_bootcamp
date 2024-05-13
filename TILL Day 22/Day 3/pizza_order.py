#program to check if the user wants s, m or l pizza and with other options as well

print("Thank you for choosing Nitesh Python pizza deliveries ")

size = input("what size pizza do you want?\n") # S, M or L
add_pepperoni = input("Do you want pepperoni?\n") # Y or N
extra_cheese = input("Do you want extra cheese?\n") # Y or N
final_bill = 0

if size == "S":
    final_bill += 100
    
elif size == "M":
    final_bill += 200

elif size == "L":
    final_bill += 500
    
else:
    print("wrong input")
    
if add_pepperoni == "Y":
    if size == "S":
        final_bill += 15
    else:
        final_bill += 25
    
if extra_cheese == "Y":
    final_bill += 10
    
print(f"Your final bill is: {final_bill}\nThank you for choosing Nitesh Python pizza delivery")