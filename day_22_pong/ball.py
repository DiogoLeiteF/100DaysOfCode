import time
from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.goto(0,0)
        self.color('White')
        self.x_step = 10
        self.y_step = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x_step
        new_y = self.ycor() + self.y_step
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y_step *= -1

    def bounce_x(self):
        self.x_step *= -1
        self.move_speed *= 0.8
        print(self.move_speed)

    def reset_position(self):
        time.sleep(0.5)
        self.move_speed = 0.1
        self.goto(0, 0)
        self.bounce_x()
