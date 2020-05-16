# A3Q3
# Author: Farzad Rahman
# Date Start: 24/03/20
# ICS3UI - 03, Ms. Harris

# Modifications:
# 03/04/20 - Created main drawing
# 04/04/20 - Added background and colours


# Source of Background Gif - https://giphy.com/gifs/space-galaxy-ygAaR0n5RsyAM


import turtle      # Calls for use of turtle library module
import random

display = turtle.Screen()
display.setup(300,250)
display.bgpic("space.gif")


colours = ('green', 'red', 'blue', 'yellow', 'purple', 'pink', 'white', 'black')


TheTurtle = turtle.Turtle()
TheTurtle.penup()
TheTurtle.goto(-90, 100)
TheTurtle.pendown()


def sketch(TheTurtle, lineLen):
    TheTurtle.speed(0.5)
    if lineLen > 30:
        TheTurtle.left(45)
        TheTurtle.forward(lineLen)
        TheTurtle.right(90)
        TheTurtle.forward(lineLen)
        TheTurtle.backward(lineLen/2)
        TheTurtle.color(random.choice(colours))
        TheTurtle.pensize(3)
        sketch(TheTurtle, lineLen-1)

sketch(TheTurtle, 75)


display.exitonclick()