import colorgram
from turtle import Turtle, Screen
import random as r

# colors = colorgram.extract('hirstdots.jpg', 30)
#
# rgb_colors = []
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     new_color = (r, g, b)
#     rgb_colors.append(new_color)
#
#
# print(rgb_colors)


color_list = [(239, 248, 244), (237, 223, 83), (207, 4, 71), (203, 73, 11), (110, 181, 218), (198, 164, 8), (238, 48, 131), (217, 162, 111), (236, 224, 4), (11, 22, 62), (25, 191, 114), (14, 28, 178), (20, 107, 176), (216, 134, 179), (6, 186, 217), (227, 169, 202), (213, 23, 153), (61, 22, 7), (121, 193, 163), (195, 13, 4), (7, 49, 27), (127, 218, 233), (27, 139, 71), (106, 87, 216), (64, 9, 35), (238, 63, 37), (144, 216, 201)]


t = Turtle()
screen = Screen()
screen.colormode(255)

position = (0, 0)
for i in range(10):
    position = t.pos()
    for i in range(10):

        t.down()
        t.dot(10, r.choice(color_list))
        t.up()
        t.fd(50)

    t.setpos(position)
    t.up()
    t.left(90)
    t.fd(50)
    t.right(90)


screen.exitonclick()