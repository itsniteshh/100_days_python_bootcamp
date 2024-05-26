vaccation = {}
game_on = True


while game_on:
    
    name = input("Enter your name: ")
    fav_vacation = input("Enter your fav vaccation spot: ")
    another_poll = input("Would another person like to respond: ")
    
    vaccation[name] = fav_vacation
    
    if another_poll == "quit":
        game_on = False
        

for n, p in vaccation.items():
    print(f"{n} would like to visit {p} sometimes")