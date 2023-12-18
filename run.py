# Space wars
import os
import random

# import the Turtle module
import turtle
# required by macos to show window
turtle.fd(0)
# sets animation speed
turtle.speed(0)
# change background colour
turtle.bgcolor("black")
# this hides the defult turtle
turtle.ht()
# this save memory 
turtle.setundobuffer(1)
# this speeds up the drawing
turtle.tracer(1)

class Sprite (turtle.Turtle):
    """
    Class set sprite for the base of the objects
    """
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__ (self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx,starty)
        self.speed = 1