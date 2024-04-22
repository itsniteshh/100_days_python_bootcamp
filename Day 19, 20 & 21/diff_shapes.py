from turtle import  Turtle, Screen
import random

colour = ["red", "blue", "green", "black", "orange", "purple"]
directions = [90, 180, 0, 270]


nit = Turtle()


for _ in range(200):
    nit.setheading(random.choice(directions))
    nit.color(random.choice(colour))
    nit.pensize(5)
    nit.speed(10)
    nit.forward(30)

screen = Screen()
screen.exitonclick()