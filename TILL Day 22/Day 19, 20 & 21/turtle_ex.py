from turtle import  Turtle, Screen

nit = Turtle()
nit.shape("turtle")
nit.color("red")
"""
nit.forward(100)
nit.left(90)
nit.forward(100)
nit.left(90)
nit.forward(100)
nit.left(90)
nit.forward(100)
nit.left(90)
"""

for _ in range(15):
    nit.forward(10)
    nit.penup()
    nit.forward(10)
    nit.pendown()


screen = Screen()
screen.exitonclick()