from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle("right_x")
l_paddle = Paddle("left_x")
ball = Ball()
screen.listen()
screen.onkey(r_paddle.go_up, "Up" )
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w" )
screen.onkey(l_paddle.go_down, "s")
scoreboard = Scoreboard()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    ball.move()

    #Detect collision with wall.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with r_paddle.
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.add_score("l_SCORE")
        game_is_on = scoreboard.game_over()
    elif ball.xcor() < -380:
        ball.reset_position()
        scoreboard.add_score("r_SCORE")
        game_is_on = scoreboard.game_over()
screen.exitonclick()