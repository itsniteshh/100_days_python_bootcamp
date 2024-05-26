end_of_loop = True

while end_of_loop:
    
    topping = input("Enter a pizza topping! ")
    
    if topping == "quit":
        end_of_loop = False
    else:
        print(f"{topping} is being added to the pizza")