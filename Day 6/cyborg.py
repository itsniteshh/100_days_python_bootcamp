# a program to guide the robot to reach the flag

def turn_right():
    move()
    
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()
    turn_left()
    turn_left()
    move()
    turn_left()

while not at_goal():
    turn_right()