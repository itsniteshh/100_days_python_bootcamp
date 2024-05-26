end_of_game = True

while end_of_game:
    age = int(input("Enter your age: "))
    
    if age < 3:
        print("Your ticket is free")
    elif age < 12:
        print("Ticket")