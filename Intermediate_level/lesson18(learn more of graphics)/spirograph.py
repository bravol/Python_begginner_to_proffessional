from random import randint
from turtle import Turtle, Screen

# Set the turtle color mode to 255 to support RGB values from 0-255
screen = Screen()
screen.colormode(255)

def random_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    return r,g,b


# Create a turtle instance
tim = Turtle()

# Set the turtle's speed
tim.speed('fastest')

def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        current_heading = tim.heading()
        tim.setheading(current_heading + size_of_gap)

draw_spirograph(5)


screen.exitonclick()