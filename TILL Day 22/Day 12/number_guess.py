from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game!")

guessed_number = random.randint(1, 100)
print(f"The guessed number is: {guessed_number}")

end_of_game = True
lives = 0

difficulty = input("Easy or Hard: ").lower() #level type

def level_choose(diff):
    """to set the difficulty level"""
    if difficulty == "easy":
        lives = 10
    else:
        lives = 5
    
    return lives
total_lives = level_choose(difficulty) #assigning total lives to a var


'''def logicals(user_num, guessed_num, tl):
    """to check the logicals"""
    if user_guess == guessed_number:
        print(f"You got it! The answer was {guessed_number}")
    elif user_guess > guessed_number:
        print(f"Guess too low")
    else:
        print(f"Guess too high")'''
        
                
while end_of_game:
    
    user_guess = int(input("Make a guess: "))
    
    if user_guess == guessed_number:
        print(f"You got it! The answer was {guessed_number}")
        end_of_game = False
        
    elif user_guess < guessed_number:
        print(f"Guess too low")
        total_lives -= 1
    else:
        print(f"Guess too high")
        total_lives -= 1
        
        
    if total_lives < 1:
        end_of_game = False
    else:
        pass