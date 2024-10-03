from random import choice, randint
from turtle import Turtle, Screen
from data import colors, directions

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r,g,b

# Create a turtle instance
tim = Turtle()

# Set the turtle's pen size and speed
tim.pensize(10)
tim.speed('fastest')

# Set the turtle color mode to 255 to support RGB values from 0-255
screen = Screen()
screen.colormode(255)

# Make the turtle draw with random colors
for _ in range(500):
    tim.color(random_color())
    tim.forward(30)
    tim.setheading(choice(directions))

# Ensure the screen doesn't close automatically
screen.exitonclick()
