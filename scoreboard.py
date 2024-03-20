from turtle import Turtle

FONT = ('Arial', 20, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color('white')

        self.lives = 3
        self.score = 0

        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-370, 380)
        self.write(f"Score: {self.score}", align='left', font=FONT)
        self.goto(280, 380)
        self.write(f"Lives: {self.lives}", align='left', font=FONT)

    def minus_life(self):
        self.lives -= 1
        self.update_score()

    def up_score(self, score: int):
        self.score += score
        self.update_score()