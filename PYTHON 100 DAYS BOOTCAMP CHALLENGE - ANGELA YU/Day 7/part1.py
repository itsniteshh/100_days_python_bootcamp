d_list = ["aardvark", "baboon", "camel"]

#1 - randomly choose a wrod from the above list
import random

choosen_word = random.choice(d_list)
print(choosen_word)

#4 - creating a placeholder to create as many blanks as there are alphabets in the word
display = ""

for l in range(len(choosen_word)):
    display += "_"
    

#2 - asking the user to guess a letter

user_guess = input("Guess a letter: ").lower()


#3 - checking if the letter the user guessed is one of the letters in our choosen word. Print righ or wrong

#5 - creating a display variable that puts the guessed letter in the right spot if the guess is correct

for letter in choosen_word:
    if user_guess == letter:
        display[letter] = user_guess
    else:
        pass