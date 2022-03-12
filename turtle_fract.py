from turtle import *

import turtle
import random
  

tur = turtle.Turtle()
  

tur.speed(10000000)
tur.hideturtle()
  
tur.getscreen().bgcolor("black")
tur.color("blue")

tur.penup()
  

tur.pendown()
  

def star(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(5):
            

            turtle.forward(size)
            star(turtle, size/3)
  

            turtle.left(216)
  
 
def triangle(turtle, size):
    if size <= 10:
        return
    else:
        for i in range(3):
            turtle.forward(size)
            triangle(turtle, size/3)

            turtle.left(120)


MINIMUM_BRANCH_LENGTH = 5
def tree(t, branch_length, shorten, angle):

    if branch_length > MINIMUM_BRANCH_LENGTH:
        t.forward(branch_length)
        new_length = branch_length - shorten

        t.left(angle)
        tree(t, new_length, shorten, angle)

        t.right(angle * 2)
        tree(t, new_length, shorten, angle)

        t.left(angle)
        t.backward(branch_length)


def koch(t, iterations, length, shortening_factor, angle):

    if iterations == 0:
        t.forward(length)

    else:

        iterations = iterations - 1
        length = length / shortening_factor
        koch(t, iterations, length, shortening_factor, angle)
        
        t.left(angle)
        koch(t, iterations, length, shortening_factor, angle)
        
        t.right(angle * 2)
        koch(t, iterations, length, shortening_factor, angle)

        t.left(angle)
        koch(t, iterations, length, shortening_factor, angle)


def square(t, iterations, length):
    if iterations == 0:
        t.forward(length)
    
    else:
        iterations = iterations - 1

        t.right(90)
        t.forward(length)
        square(t, iterations, length)





'''tur.penup()
tur.goto(-350, 0)
tur.pendown()
'''

tur.width(2)

'''for i in range(3):
    koch(tur, 4, 200, 3, 60)'''

square(tur, 4, 200)

tur.setheading(90)

turtle.mainloop()