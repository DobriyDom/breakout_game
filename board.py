from turtle import Turtle


class Board(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('grey')
        self.shapesize(stretch_wid=1, stretch_len=10)
        self.penup()
        self.pensize(5)
        self.goto(383, -453)
        self.pendown()
        self.goto(383, 453)
        self.goto(383, 343)
        self.goto(-383, 343)
        self.goto(-383, 453)
        self.goto(-383, -453)
        self.penup()
        self.reset_pos()

    def reset_pos(self):
        self.goto(0, -415)

    def move_right(self):
        if self.xcor() <= 270:
            self.goto(self.xcor() + 15, -415)

    def move_left(self):
        if self.xcor() >= -270:
            self.goto(self.xcor() - 15, -415)