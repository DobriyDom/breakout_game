from turtle import TurtleScreen, Screen
from ball import Ball
from board import Board
from time import sleep
from panels import Panels
from scoreboard import Scoreboard


class BreakoutGameUI:
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=900)
        self.screen.title('Breakout')
        self.screen.bgcolor('#333333')
        self.screen.tracer(0)

    def update(self):
        self.screen.update()


game = BreakoutGameUI()

ball = Ball()
board = Board()
panels = Panels()
scoreboard = Scoreboard()

game.screen.listen()
game.screen.onkey(fun=board.move_right, key='Right')
game.screen.onkey(fun=board.move_left, key='Left')

game_on = True
while game_on:
    ball.move()
    game.update()
    if ball.xcor() >= 363 or ball.xcor() <= -363:
        ball.bounce_x()
    elif ball.ycor() <= -440:
        ball.reset_pos()
        board.reset_pos()
        scoreboard.minus_life()
    elif ball.ycor() >= 330 or ball.ycor() <= -400 and ball.distance(board) < 125:
        ball.bounce_y()
    panels.touch_sides(ball, scoreboard)

    if not panels.is_active() or not scoreboard.lives:
        game_on = False
    sleep(ball.move_speed)

game.screen.exitonclick()
