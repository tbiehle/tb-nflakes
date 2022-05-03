from turtle import *

import turtle
from mpmath import tan, pi, sin, cos, radians
# important for scale factor calculations


# Explanation of Turtle module: 
# Imagine that the turtle is a pen on paper. We can give the turtle step-by-step instructions 
# on how to move, where to go, and when/what to draw. By giving precise instructions to the 
# turtle based on algorithms, we can draw the n-flake.

# |-- USER INPUT --|
sides = int(input('How many sides should the n-flake have? (note: high values take a while to render!) '))
iterations = int(input('How many iterations should be processed?: '))
save=''
while True:
    save = input('save the image? [y/n]')
    if save=='y' or save=='n':
        break

draw = ''
while True:
    draw = input('Show the drawing process? (not recommended for high # of iterations/sides) [y/n]: ')
    if draw =='y' or draw=='n':
        break

# |-- TURTLE MODULE INITIATION --|
tur = turtle.Turtle()

screenwidth = 1000
screenheight = 1000
tur.screen.setup(screenwidth, screenheight)

tur.speed(0)
tur.hideturtle()

# |-- MAIN N-FLAKE FUNCTION --|
def ngon(t, sides, length, factor, iterations):
    """
        This function uses recursion to draw the n-flake. It first goes to the deepest iteration level as
        defined by the user, then draws the smallest instance of the shape. Once this happens, it goes back
        out to the previous level, moves forward again, and draws another shape. It does this at each 
        level of iteration, for each side of the shape, until it is finished.
    """
    if iterations == 0:   # If turtle is at lowest iteration level, go to previous 
        return            # iteration level (prevents infinite recursion).
    else:
        iterations -= 1   # go down an iteration level for next function call
        for i in range(sides):
            t.penup()
            if iterations == 0:  # if at lowest level of iteration, draw the line. this allows the fractal to be composed 
                t.pendown()      # only of the smallest instace of the shape, instead of every level being drawn.
            t.left(360/sides)    # turn left degrees to make shape
            t.forward(length)    # draw one side of the shape
            ngon(t, sides, length / factor, factor, iterations) # recursively call the function.

# |-- SET PARAMETERS --|
tur.penup()

length = (screenwidth - 150) * (2*(sin(radians(90/sides)))) # set side length of polygon

rad = length / (2 * sin(radians(180/sides)))    # calculate length of radius of polygon (center to circumcircle)
apot = length / (2 * tan(radians(180/sides)))   # calculate length of apothem (center to midpoint of side)

tur.sety(-(apot + rad) / 2)  # set turtle's y position on the canvas to half its height
tur.setx(length / 2)         # set turtle's x position on the canvas to half its side width
'''
The following formula was found on https://en.wikipedia.org/wiki/N-flake#In_two_dimensions.
The formula returns the scale factor that each side should be multiplied by between iterations.
This enables each smaller iteration of the fractal to be perfectly nested inside each previous
iteration, taking up the exact amount of space to be perfectly tangent with all other shapes.
'''
factor = 2 * (1 + sum(cos((2 * pi * i)/sides) for i in range(1, int(sides/4) + 1)))


# |-- BEGIN DRAWING --|

tur.pendown()

if draw == 'n':             # if user doesn't want to see the drawing process
    turtle.tracer(0, 0)     # stop the screen from updating
turtle.tracer(0,0)
ngon(tur, sides, length, factor, iterations) # call function to draw fractal

turtle.tracer(1, 1)         # final step

if save == 'y':
    ts = tur.getscreen()
    ts.getcanvas().postscript(file='fractal.ps')


turtle.mainloop()           # draw updates to canvas
turtle.update()             # display fractal