# Space wars
import os
import random
import pygame


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


class Game():
    """
    Game class for the game rules and lives
    """
    def __init__(self):
        self.level = 1
        self.score = 0
        self.state = "playing"
        self.pen = turtle.Turtle()
        self.lives = 3
    
    def draw_border(self):
        # draw border
        self.pen.speed(0)
        self.pen.color("white")
        self.pen.pensize(3)
        self.pen.penup()
        self.pen.goto(-300, 300)
        self.pen.pendown()
        for side in range(4):
            self.pen.fd(600)
            self.pen.rt(90)
        self.pen.penup()
        self.pen.ht()


# Creat game object
game = Game()

# Draw game border
game.draw_border()
        

# creat my sprites
player = Player("triangle", "green", 0,0)

# Keyboard binding
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()

# Main game loop
while True:
    player.move()
else:
    print("Game has stopped working")








delay = raw_input("Press enter to finish.> ")