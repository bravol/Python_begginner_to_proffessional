import random
from turtle import Turtle, Screen


screen = Screen()

screen.setup(width=500,height=400)

user_bet = screen.textinput(title='Make your bet', prompt="Which turtle will win the race? Enter the color: ")
colors = ['red','orange','yellow', 'green', 'blue', 'purple']
y_position = [-70,-40, -10, 20, 50,80]
all_turtle = []
is_race_on = False

for turtle_index in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y= y_position[turtle_index])
    all_turtle.append(new_turtle)

# creating a random number
if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor() >= 230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won!, the {winning_color} turtle is the winner")
            else:
                print(f"You've lost the game!, the {winning_color} turtle is the winner")
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()