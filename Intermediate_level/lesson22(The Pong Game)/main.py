from turtle import Screen
from paddle import  Paddle
from ball import Ball
from score_board import ScoreBoard
import time

screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('The Pong Game')
screen.tracer(0) #turn off the animation

# creating two paddles and a ball
right_paddle = Paddle((350,0))
left_paddle = Paddle((-350,0))
ball = Ball()
score_board = ScoreBoard()


screen.listen()
screen.onkey(right_paddle.go_up, 'Up')
screen.onkey(right_paddle.go_down,'Down')

screen.onkey(left_paddle.go_up, 'w')
screen.onkey(left_paddle.go_down,'s')


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed) # it controls the speed
    screen.update()
    ball.move()

#     detecting the collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

#   detect collision with both paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

#   detect when the Right paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.increase_left_point()

#   detect when the Left paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.increase_right_point()




screen.exitonclick()