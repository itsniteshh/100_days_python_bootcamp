from turtle import Screen, Turtle

#Step 1-  creating screen
screen = Screen()
screen.bgcolor("white")
screen.setup(width= 800, height= 700)
screen.title("Ping Pong")

paddle = Turtle("square")
paddle.width(20)
paddle.color("red")
paddle.shapesize(stretch_wid= 5, stretch_len= 1)
paddle.penup()
paddle.goto(350, 0)


def go_up():
    new_y = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), new_y)
    
def go_down():
    new_y = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), new_y)
    
    
    
screen.listen()
screen.onkey(go_up, "Up")
screen.onkey(go_down, "Down")







screen.exitonclick()