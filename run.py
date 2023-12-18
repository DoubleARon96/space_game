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
        turtle.Turtle.__init__(self, shape = spriteshape)
        self.speed(0)
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx,starty)
        self.speed = 1
# this is the move function 
    def move(self):
        self.fd(self.speed)

class Player(Sprite):
    """
    Player class for movement colour and start point 
    """
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__ (self, spriteshape, color, startx, starty)
        self.speed = 4
        self.lives = 3

    def turn_left(self):
        self.lt(45)
    
    def turn_right(self):
        self.rt(45)
    
    def accelerate(self):
        self.speed += 1

    def decelerate(self):
        self.speed -= 1

class Bullet(turtle.sprite.Sprite):
    def __init__(self, start_pos, direction, check, exclude):
        turtle.sprite.Sprite.__init__(self)
        self.image = turtle.Surface((10, 10))
        self.image.fill((255, 225, 0))
        self.rect = self.image.get_rect((center=start_pos))
        self.direction = direction
        self.speed = 10
        self.damage = 5
        self.destroy = False
        self.check = check
        self.exclude = exclude
    #this draws the bullet on screen
    def draw(self, screen):
        screen.blit(self.image, self.rect)
        
    def update(self):