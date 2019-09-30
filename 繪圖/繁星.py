#  Copyright (c) 2019.
#  繁星.py
#
#
import turtle
import random
for i in range(50):
    x=random.randrange(-100,100)*5
    y=random.randrange(-100,100)*5
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
    turtle.forward(100)
    turtle.right(144)
turtle.done()

