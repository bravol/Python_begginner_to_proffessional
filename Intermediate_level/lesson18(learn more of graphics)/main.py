from turtle import Turtle, Screen

timmy_the_turtle = Turtle()


timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')
def create_squire():
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

for _ in range(4):
    create_squire()

import heroes
import villains






screen = Screen()
screen.exitonclick()

# python tuple
my_tuple = (1,2,3) # you cannot change/edit the tuple
print(my_tuple[0])