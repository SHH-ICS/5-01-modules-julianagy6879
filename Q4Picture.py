# Using the pygame library, draw a simple picture. 
# It can be anything you like, but you must use at least 2 different types of shapes and 3 different colors.
import pygame

from pygame import Color, Rect
from pygame import draw
from pygame import display

SCREEN_SIZE = (500, 500)

# initialize pygame modules
pygame.init()

# get a surface for graphics display
gameDisplay = display.set_mode(SCREEN_SIZE)

# background - color of the sky
gameDisplay.fill(Color('lightblue'))

# draw a house with a roof
draw.rect(gameDisplay, Color('yellow'), Rect(200, 400, 600, 400))
draw.polygon(gameDisplay, Color('orange'), [(300, 400), (800, 400), (300, 100)])

# draw green grass
draw.rect(gameDisplay, Color('purple'), Rect(600, 400, 500, 400))

# draw a moon
draw.circle(gameDisplay, Color('beige'), (100, 100), 300)

# draw a sun
draw.circle(gameDisplay, Color('black'), (250, 200), 50)

# show the graphics on the screen
display.flip()

# Wait for user input before closing the window
input("Press enter to exit")