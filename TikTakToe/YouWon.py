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


def SaSundSpass():
    turtle.setup(width=600, height=500)
    turtle.reset()
    turtle.hideturtle()
    turtle.speed(20)

    turtle.bgcolor('black')

    c = 0
    x = 0

    colors = [
        # reddish colors
        (1.00, 0.00, 0.00), (1.00, 0.03, 0.00), (1.00, 0.05, 0.00), (1.00, 0.07, 0.00), (1.00, 0.10, 0.00),
        (1.00, 0.12, 0.00), (1.00, 0.15, 0.00), (1.00, 0.17, 0.00), (1.00, 0.20, 0.00), (1.00, 0.23, 0.00),
        (1.00, 0.25, 0.00), (1.00, 0.28, 0.00), (1.00, 0.30, 0.00), (1.00, 0.33, 0.00), (1.00, 0.35, 0.00),
        (1.00, 0.38, 0.00), (1.00, 0.40, 0.00), (1.00, 0.42, 0.00), (1.00, 0.45, 0.00), (1.00, 0.47, 0.00),
        # orangey colors
        (1.00, 0.50, 0.00), (1.00, 0.53, 0.00), (1.00, 0.55, 0.00), (1.00, 0.57, 0.00), (1.00, 0.60, 0.00),
        (1.00, 0.62, 0.00), (1.00, 0.65, 0.00), (1.00, 0.68, 0.00), (1.00, 0.70, 0.00), (1.00, 0.72, 0.00),
        (1.00, 0.75, 0.00), (1.00, 0.78, 0.00), (1.00, 0.80, 0.00), (1.00, 0.82, 0.00), (1.00, 0.85, 0.00),
        (1.00, 0.88, 0.00), (1.00, 0.90, 0.00), (1.00, 0.93, 0.00), (1.00, 0.95, 0.00), (1.00, 0.97, 0.00),
        # yellowy colors
        (1.00, 1.00, 0.00), (0.95, 1.00, 0.00), (0.90, 1.00, 0.00), (0.85, 1.00, 0.00), (0.80, 1.00, 0.00),
        (0.75, 1.00, 0.00), (0.70, 1.00, 0.00), (0.65, 1.00, 0.00), (0.60, 1.00, 0.00), (0.55, 1.00, 0.00),
        (0.50, 1.00, 0.00), (0.45, 1.00, 0.00), (0.40, 1.00, 0.00), (0.35, 1.00, 0.00), (0.30, 1.00, 0.00),
        (0.25, 1.00, 0.00), (0.20, 1.00, 0.00), (0.15, 1.00, 0.00), (0.10, 1.00, 0.00), (0.05, 1.00, 0.00),
        # greenish colors
        (0.00, 1.00, 0.00), (0.00, 0.95, 0.05), (0.00, 0.90, 0.10), (0.00, 0.85, 0.15), (0.00, 0.80, 0.20),
        (0.00, 0.75, 0.25), (0.00, 0.70, 0.30), (0.00, 0.65, 0.35), (0.00, 0.60, 0.40), (0.00, 0.55, 0.45),
        (0.00, 0.50, 0.50), (0.00, 0.45, 0.55), (0.00, 0.40, 0.60), (0.00, 0.35, 0.65), (0.00, 0.30, 0.70),
        (0.00, 0.25, 0.75), (0.00, 0.20, 0.80), (0.00, 0.15, 0.85), (0.00, 0.10, 0.90), (0.00, 0.05, 0.95),
        # blueish colors
        (0.00, 0.00, 1.00), (0.05, 0.00, 1.00), (0.10, 0.00, 1.00), (0.15, 0.00, 1.00), (0.20, 0.00, 1.00),
        (0.25, 0.00, 1.00), (0.30, 0.00, 1.00), (0.35, 0.00, 1.00), (0.40, 0.00, 1.00), (0.45, 0.00, 1.00),
        (0.50, 0.00, 1.00), (0.55, 0.00, 1.00), (0.60, 0.00, 1.00), (0.65, 0.00, 1.00), (0.70, 0.00, 1.00),
        (0.75, 0.00, 1.00), (0.80, 0.00, 1.00), (0.85, 0.00, 1.00), (0.90, 0.00, 1.00), (0.95, 0.00, 1.00)
    ]

    while x < 1000:
        idx = int(c)
        color = colors[idx]
        turtle.color(color)
        turtle.forward(x)
        turtle.right(98)
        x = x + 1
        c = c + 0.1

    turtle.exitonclick()


