from turtle import *

import turtle
from mpmath import sqrt, tan, cot, pi, sec, sin, cos

sides = int(input('How many sides should the n-flake have? [3-10]'))

tur = turtle.Turtle()
  
colors = ['red', 'orange', 'green', 'blue', 'purple', 'pink', 'gold', 'black']

tur.screen.setup(1000, 1000)

tur.speed(10000000)
tur.hideturtle()
  
tur.getscreen().bgcolor("white")


def ngon(t, sides, length, factor, iterations):

    if iterations != 0:
        iterations -= 1
        for i in range(sides):
            t.penup()
            # t.color(colors[int(length % sides)])
            if iterations == 0:
                t.pendown()
            t.left(360/sides)
            t.forward(length)
            ngon(t, sides, length / factor, factor, iterations)

    else:
        return


tur.penup()

length = 200

rad = length / (2 * sin(180/sides))
apot = length / (2 * tan(180/sides))
tur.sety(-(rad + apot) / 2)

factor = 2 * (1 + sum(cos((2 * pi * i)/sides) for i in range(1, int(sides/4) + 1)))

tur.setx(length / 2)
tur.pendown()


turtle.tracer(0, 0)
ngon(tur, sides, length, factor, 5)


turtle.mainloop()
turtle.update()