
import random

############### Blackjack Project #####################

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10] #11 is the ace
end_of_game = True
choosen_cards = []

def choosing_cards():
    """randomly choosing cards """
    first_guess = random.choices(cards, k = 2)
    return first_guess

def second_card():
    """choosing second card"""
    other_guess = random.choice(cards)
    return other_guess

def first_user(choosed):
    user_guess = choosing_cards()
    user_total = 0
    for nums in user_guess:
        user_total += nums
        
    return user_guess, user_total

def first_com(choosed):
    com_total = 0
    com_guess = choosing_cards()
    for nums in com_guess:
        com_total += nums
    
    return com_guess, com_total

    
while end_of_game:
    
    another_card = input("Do you want to play a game of Blackjack: ").lower()
    
    if another_card == "no":
        end_of_game = False
    else:
        first_user(choosing_cards)
        first_com(choosing_cards)
    
    
    
            
    

    
    
