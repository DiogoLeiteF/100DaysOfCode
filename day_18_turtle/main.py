from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape('turtle')


screen = Screen()
screen.colormode(255)

# for i in range(4):
#     tim.forward(100)
#     tim.right(90)


# dashed line
# for i in range(15):
#     tim.forward(10)
#     tim.up()
#     tim.forward(10)
#     tim.down()


# def draw_shape(sides, color):
#     tim.color(color)
#     for i in range(sides):
#         angle = 360 / sides
#         tim.forward(100)
#         tim.right(angle)


colors = ['red', 'blue', 'pink', 'gray', 'violet', 'green', 'brown', 'orange']


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r, g, b)
    return rand_color


# for i in range(3, 20):
#     draw_shape(i, random.choice(colors))

choices = ['f', 'b', 'l', 'r']


# random walk
def rand_move(steps, direction):
    tim.width(5)
    tim.speed(0)
    tim.pencolor(random_color())

    if direction == 'f':
        tim.forward(steps)
    elif direction == 'b':
        tim.backward(steps)
    elif direction == 'r':
        tim.right(90)
        tim.forward(steps)
    elif direction == 'l':
        tim.left(90)
        tim.forward(steps)


for i in range(100):
    rand_move(15, random.choice(choices))


screen.exitonclick()

