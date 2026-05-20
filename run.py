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
turtle.tracer(0)


class Sprite (turtle.Turtle):
    """
    Class set sprite for the base of the objects
    """
    def __init__(self, spriteshape, color, startx, starty):
        turtle.Turtle.__init__(self, shape=spriteshape)
        self.speed(0)      # turtle animation speed
        self.movespeed = 1 # your movement speed
        self.penup()
        self.color(color)
        self.fd(0)
        self.goto(startx, starty)

# this is the move function
    def move(self):
        self.fd(self.movespeed)


class Player(Sprite):
    """
    Player class for movement colour and start point 
    """
    def __init__(self, spriteshape, color, startx, starty):
        Sprite.__init__(self, spriteshape, color, startx, starty)
        self.movespeed = 1
        self.lives = 3

    def turn_left(self):
        self.lt(45)
    
    def turn_right(self):
        self.rt(45)
    
    def accelerate(self):
        self.movespeed += 1

    def decelerate(self):
        if self.movespeed > 0:
            self.movespeed -= 1



class Bullet(turtle.Turtle):
    """
    A class to manage bullets fired from a sprite
    """
    def __init__(self):
        """Create a bullet object at the sprite's current position"""
        super().__init__()
        self.color("red")
        self.shape("square")
        self.penup() 
        self.speed = 0
        self.hideturtle()
    
    def bullet_fired(self, x, y):
        """
        Show and move the bullet up the screen
        """
        self.goto(x, y)
        self.showturtle()
        # show the bullet
        #self.showturtle() 
        # set the position of the bullet
        #self.goto(x, y) 
        # move the bullet forward
        #self.forward(20)
        # check if the bullet is out of the screen 
        #if self.ycor() > 280: 
        #    self.hideturtle() 
        # hide the bullet

   
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


# Create game object
game = Game()

# Draw game border
game.draw_border()
 
# create my sprites
player = Player("triangle", "green", 0, 0)

bullet = Bullet()

def fire_bullet():
    x = player.xcor()
    y = player.ycor()
    bullet.setheading(player.heading())
    bullet.bullet_fired(x, y)



turtle.onkey(fire_bullet, "space")


# Keyboard binding
turtle.onkey(player.turn_left, "Left")
turtle.onkey(player.turn_right, "Right")
turtle.onkey(player.accelerate, "Up")
turtle.onkey(player.decelerate, "Down")
turtle.listen()

# Main game loop
while True:
    player.move()
    # Keep player inside border
    if player.xcor() > 290:
        player.setx(290)
    if player.xcor() < -290:
        player.setx(-290)
    if player.ycor() > 290:
        player.sety(290)
    if player.ycor() < -290:
        player.sety(-290)

    # Move bullet continuously
    if bullet.isvisible():
        bullet.forward(20)
        if bullet.ycor() > 280:
            bullet.hideturtle()

    turtle.update()



run.delay = raw_input("Press enter to finish.> ")