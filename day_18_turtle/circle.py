from turtle import Turtle, Screen
import random

t = Turtle()
t.speed('fastest')
screen = Screen()
screen.colormode(255)


def random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    rand_color = (r, g, b)
    return rand_color


def draw (gap):
    for i in range(360//gap):
        t.color(random_color())
        t.circle(100)
        t.setheading(t.heading() + gap)


draw(5)
screen.exitonclick()