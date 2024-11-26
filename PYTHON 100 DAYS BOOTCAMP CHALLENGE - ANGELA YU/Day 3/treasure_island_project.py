treasure_island = '''

                                                             
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/________
*******************************************************************************
 
'''


print(treasure_island)
print("Welcome to the Treasure Island program")

direction = input("You're at a cross road. Where do you want to go? ")

if direction == "right":
    print("You have come to a lake. There is an island in the middle of the lake.")
    
    wait = input("Type 'wait' to wait for the boat or 'swim' ")
    if wait == "swim":
        print("You arrive at an island swimming. There is a huge kingdom with 3 doors.")
        
        door = input("one red, one yellow and one blue. Which color do you choose? ")
        if door == "red":
            print("You win! You found a bag full of gold")
        elif door == "yellow":
            print("You found a room full with fire, Game over!")
        else:
            print("Alien came and abducted you! Game Over")
        
    else:
        print("Monsters came and attacked you, Game over!")

else:
    print("You got lost in a jungle full of demons! You lose")