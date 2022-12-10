from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('My Snake Game')
screen.tracer(0)
screen.update()

scoreboard = Scoreboard()
snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, 'Up')
screen.onkey(snake.down, 'Down')
screen.onkey(snake.left, 'Left')
screen.onkey(snake.right, 'Right')

sleep_time = 0.1

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(sleep_time)
    snake.move()

    # Detect collision with food.
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extend()
        scoreboard.add()
        # level up
        sleep_time *= 0.99

    # Detect collision with wall.
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        scoreboard.reset()
        snake.reset()
        sleep_time = 0.1

    # Detect collision with tail
    # if head collide with any segment in the tail:
    for segment in snake.segments[1:]: # the first is the head
        if snake.head.distance(segment) < 10:
            scoreboard.reset()
            snake.reset()
            sleep_time = 0.1


# scoreboard.game_over()
screen.exitonclick()