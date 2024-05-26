end_of_game = True

while end_of_game:
    age = input("Enter your age: ")
    
    if age == "quit":
        end_of_game = False
    else:
        age = int(age)
        if age < 3:
            print("Your ticket is free")
        elif age < 12:
            print("Ticket costs 10$")
        else:
            print("Ticket costs 15$")
        
    