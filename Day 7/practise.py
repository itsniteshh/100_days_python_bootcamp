import random
word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(word_list)
word_length = len(chosen_word)
print(chosen_word)

#2 - assigning "_" according to the num of chars
display = []
for w in chosen_word:
    display += "_"

#3 - getting user guess and checking if its in chosen word
while True:
    user_guess = input("Enter your guess:") #alphabet

    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == user_guess:
            display[position] = letter
    
    if 

print(display) 