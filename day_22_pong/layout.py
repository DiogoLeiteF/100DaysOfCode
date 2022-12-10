from turtle import Turtle


class Layout(Turtle):
    def __init__(self):
        super(Layout, self).__init__()
        self.shape('square')
        self.hideturtle()
        self.color('grey')
        self.score_marks()
        self.side_marks()

    def score_marks(self):
        self.pensize(3)
        self.penup()
        self.goto(360, 300)
        self.pendown()
        self.goto(360, -300)
        self.penup()
        self.goto(-360, -300)
        self.pendown()
        self.goto(-360, 300)
        self.penup()

    def side_marks(self):
        self.pensize(10)
        self.goto(-400, 300)
        self.pendown()
        self.goto(400, 300)
        self.pendown()
        self.goto(400, 300)
        self.penup()
        self.goto(400, -300)
        self.pendown()
        self.goto(-400, -300)
        self.penup()
