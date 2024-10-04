from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()

def move_forwards():
    tim.forward(10)

def move_backwards():
    tim.backward(10)

def turn_left():
    new_heading =tim.heading() + 10
    tim.setheading(new_heading)

def turn_right():
    new_heading =tim.heading() - 10
    tim.setheading(new_heading)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

# tell a screen to start listening
screen.listen()
screen.onkey(move_forwards, 'w')
screen.onkey(move_backwards, 's')
screen.onkey(turn_left, 'l')
screen.onkey(turn_right, 'r')
screen.onkey(clear, 'c')


# the screen does not disappear
screen.exitonclick()