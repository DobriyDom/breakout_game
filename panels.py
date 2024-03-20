from turtle import Turtle
from ball import Ball
from scoreboard import Scoreboard
import numpy.random as rand
import numpy as np

SIZE_PER_PANEL = 7.4


def get_sizes():
    rand.seed(1)
    sizes = rand.randint(6, 14, size=(4, 10))
    new_sizes = []
    for row in sizes:
        arr = []
        for item in row:
            item = item / sum(row) * 100
            arr.append(item)
        new_sizes.append(arr)
    new_sizes = np.array(new_sizes)
    for row in new_sizes:
        s = int(round(sum([item - int(item) for item in row]), 0))
        row[np.argmin(row)] = row[np.argmin(row)] + s
    new_sizes = np.array(new_sizes, dtype=int)
    return new_sizes


def get_panels():
    panel_sizes = get_sizes()
    panels = []
    prev_pos_y = 310
    color = iter(['red', 'orange', 'yellow', '#90ee90'])
    type = iter([4, 3, 2, 1])
    for row in panel_sizes:
        prev_pos_x = -380
        cur_color = next(color)
        cur_type = next(type)
        for size in row:
            prev_pos_x += size / 2 * SIZE_PER_PANEL
            panel = Panel()
            panel.color(cur_color)
            panel.goto(prev_pos_x, prev_pos_y)
            panel.shapesize(stretch_wid=3, stretch_len=size/20 * SIZE_PER_PANEL, outline=1)
            panels.append({'type': cur_type, 'panel': panel, 'size': size, 'active': True})
            prev_pos_x += size / 2 * SIZE_PER_PANEL + 2
        prev_pos_y -= 65
    return panels


class Panel(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.penup()


class Panels:
    def __init__(self):
        self.panels = get_panels()

    def touch_sides(self, ball: Ball, scoreboard: Scoreboard):
        for panel in self.panels:
            if panel['panel'].xcor() - panel['size'] * SIZE_PER_PANEL / 2 - 10 <= ball.xcor() <= panel['panel'].xcor() + panel['size'] * SIZE_PER_PANEL / 2 + 10\
                    and (panel['panel'].ycor() - 30 - ball.ycor() - 10 <= 10 or panel['panel'].ycor() + 30 - ball.ycor() + 10 <= 10)\
                    and panel['active']:
                panel['active'] = False
                panel['panel'].hideturtle()
                scoreboard.up_score(panel['type'])
                ball.bounce_y()
                break
            if panel['panel'].ycor() + 30 + 10 >= ball.ycor() >= panel['panel'].ycor() - 30 - 10\
                    and (abs(panel['panel'].xcor() - panel['size'] * SIZE_PER_PANEL / 2 - ball.xcor() - 10) <= 10 or abs(panel['panel'].xcor() + panel['size'] * SIZE_PER_PANEL / 2 - ball.xcor() + 10) <= 10)\
                    and panel['active']:
                panel['active'] = False
                panel['panel'].hideturtle()
                scoreboard.up_score(panel['type'])
                ball.bounce_x()
                break

    def is_active(self):
        return any([panel['active'] for panel in self.panels])



