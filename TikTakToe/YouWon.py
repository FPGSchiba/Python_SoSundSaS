# You Won --> Der Schluss-Screen von TikTakToe
# Author: Das Internet mit Ergänzungen von Jann Erhardt
# Version 1.0
# Changes:
#   - 16.04.2020 --> Init / Jann Erhardt

import turtle
from random import randint


def YouWon():
    t = turtle.Turtle()
    t.hideturtle()

    turtle.bgcolor('black')

    x = 0

    while x < 1600:
        r = randint(0, 255)
        g = randint(0, 255)
        b = randint(0, 255)
        turtle.colormode(255)
        t.pencolor(r, g, b)
        t.speed(10 + x)
        t.fd(100 + x)
        t.rt(90.911)

        x = x + 1

    turtle.exitonclick()
