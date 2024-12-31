from random import shuffle

ball = ['-', '-', 'O']

def shuffle_ball(ball):
    shuffle(ball)
    return ball

ball_pos = shuffle_ball(ball)

userguess = int(input("Enter your guessed position:(1, 2, 3) "))- 1

def guess_checker(ball_pos, userguess):
    
    if ball_pos[userguess] == "O":
        print("Correct guess")
    else:
        print(f'Wrong guess! Ball is at position {ball_pos}')
              
              

guess_checker(ball_pos, userguess)