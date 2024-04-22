import time
from turtle import Turtle, Screen

# setting screen
screen = Screen()
screen.setup(width= 800, height = 700)
screen.bgcolor("black")
screen.title("Nitesh's Snake Game!")
screen.tracer(0)


#Step 1 - creating the snake

starting_pos = [(0, 0), (-20, 0), (-40, 0)]
segments = []

for pos in starting_pos:
    snake = Turtle("square")
    snake.color("white")
    snake.penup()
    snake.goto(pos)
    segments.append(snake)
"""
snake = Turtle(("square"))
snake.color("white")
snake = Turtle(("square"))
snake.color("white")
snake.goto(-20, 0)
snake = Turtle(("square"))
snake.color("white")
snake.goto(-40, 0)
"""


# step 2 - moving the snake
end_of_game = True

while end_of_game:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(start=2, stop=0, step=-1):
        seg.forward(20)



screen.exitonclick()