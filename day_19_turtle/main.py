from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)


def move_back():
    tim.backward(10)


def rotate_clockwise():
    tim.right(10)


def rotate_counter_clockwise():
    tim.left(10)


def clear():
    tim.clear()
    tim.up()
    tim.home()
    tim.down()


screen.onkey(key='w', fun=move_forward)
screen.onkey(key='s', fun=move_back)
screen.onkey(key='d', fun=rotate_clockwise)
screen.onkey(key='a', fun=rotate_counter_clockwise)
screen.onkey(key='c', fun=clear)

screen.listen()

screen.exitonclick()
