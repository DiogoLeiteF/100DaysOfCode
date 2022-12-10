from turtle import Turtle
ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.penup()
        self.hideturtle()
        self.color('white')
        self.goto(0, 270)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f'Score: {self.score} ||| High Score: {self.high_score}', False, align=ALIGNMENT, font=FONT)

    def add(self):
        self.score += 1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
        self.score = 0
        self.update_scoreboard()
        with open("data.txt", mode="w") as data:
            data.write(f"{self.high_score}")

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write('GAME OVER', False, align=ALIGNMENT, font=FONT)
