from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
from layout import Layout
import time


screen = Screen()
screen.setup(width=1000, height=800)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)

r_paddle = Paddle(350, 0)
l_paddle = Paddle(-350, 0)
ball = Ball()

scoreboard = Scoreboard()

layout = Layout()

screen.listen()
screen.onkeypress(r_paddle.go_up, 'Up')
screen.onkeypress(r_paddle.go_down, 'Down')
screen.onkeypress(l_paddle.go_up, 'w')
screen.onkeypress(l_paddle.go_down, 's')
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')

game_is_on = True
bounce = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() >= 280 or ball.ycor() <= -280:
        ball.bounce_y()

    # Detect collision with paddles:
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        if bounce:
            ball.bounce_x()
        bounce = False
    else:
        bounce = True

    # Detect ball passing r_paddle
    if ball.xcor() >= 360:
        ball.reset_position()
        scoreboard.l_point()

    # Detect ball passing l_paddle
    if ball.xcor() <= -360:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
