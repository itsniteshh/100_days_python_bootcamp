rock = '''
ROCK
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
PAPER
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
SCISSORS
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

#storing pics into list

game = [rock, paper, scissors]

# USER GUESS
user_guess = int(input("Enter your guess: 0 for rock, 1 for paper or 2 for scissor\n"))
user_chose = game[user_guess]
print(f"You choose:\n{user_chose}")


#getting computer guess using random
com_guess = random.randint(0, 2)
com_chose = game[com_guess]
print(f"Com choose:\n{com_chose}")

# rock beats scissors, scissors beat paper, paper beats rock

if user_guess == com_guess:
    print("Match drawn")
    
elif user_guess == 0 and com_guess == 2:
    print("User wins")
    
elif user_guess == 2 and com_guess == 1:
    print("User wins")
elif user_guess == 1 and com_guess == 0:
    print("User wins")     
else:
    print("You lose...... Com Wins!")