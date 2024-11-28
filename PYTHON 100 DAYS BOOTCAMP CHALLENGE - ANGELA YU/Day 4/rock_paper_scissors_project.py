import random

game = ["rock", "paper", "scissors"]
player = input("Player, Enter your name: ")

#com guess - I can choose random.choice but that'll be easy
com = random.randint(0, len(game)-1)
com_guess = game[com]

# User guess - avoiding input function for this one
user = random.randint(0, len(game)-1)
user_guess = game[user]

print(f"{player} chose {user_guess}, Com chose {com_guess}.")

# game rule - rock beats scissors, scissors beat paper, paper beats rock
# conditions below
'''
if user_guess == com_guess:
    print("It's a draw!")
    
elif user == 0 and com == 2:
    print(f"{player} wins")
    
elif com == 0 and user == 2:
    print(f"{player} chose {user_guess}, Com chose {com_guess}. Com wins")
    
elif com > user:
    print(f"{player} chose {user_guess}, Com chose {com_guess}. Com wins")
    
elif user > com:
    print(f"{player} chose {user_guess}, Com chose {com_guess}. {player} wins")
    
'''

# Game logic with separate conditions
if user_guess == com_guess:
    print("It's a draw!")

elif user_guess == "rock" and com_guess == "scissors":
    print(f"{player} wins! Rock smashes Scissors.")

elif user_guess == "scissors" and com_guess == "papers":
    print(f"{player} wins! Scissors cut Paper.")

elif user_guess == "papers" and com_guess == "rock":
    print(f"{player} wins! Paper wraps Rock.")

elif com_guess == "rock" and user_guess == "scissors":
    print("Com wins! Rock smashes Scissors.")

elif com_guess == "scissors" and user_guess == "papers":
    print("Com wins! Scissors cut Paper.")

elif com_guess == "papers" and user_guess == "rock":
    print("Com wins! Paper wraps Rock.")
    