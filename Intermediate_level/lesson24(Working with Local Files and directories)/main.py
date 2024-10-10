from turtle import  Screen
import time
from snake import Snake
from food import Food
from score_board import ScoreBoard

screen = Screen()
screen.setup(width = 600, height = 600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0) #turn off the animation

snake = Snake()
food = Food()
scoreBoard =ScoreBoard()

# listeners
screen.listen()
screen.onkey(snake.up,'Up')
screen.onkey(snake.down,'Down')
screen.onkey(snake.left,'Left')
screen.onkey(snake.right,'Right')


#2. move the snake
game_is_on = True



while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

#     collision with food
    if snake.head.distance(food) < 15:
        food.random_location()
        scoreBoard.increase_score()
        snake.extend_body()

#     detect collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreBoard.reset()
        snake.reset()


#       detect collision with the tail  USING SLICING
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            scoreBoard.reset()
            snake.reset()





screen.exitonclick()