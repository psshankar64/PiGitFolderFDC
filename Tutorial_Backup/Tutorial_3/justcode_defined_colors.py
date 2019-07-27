# This script will fill the display surface a random color

import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *

#Define some standard colors
FUCHSIA = (255, 0, 255)
PURPLE = (128, 0, 128)
TEAL = (0, 128, 128)
LIME = (0, 255, 0)
GREEN = (0, 128, 0)
OLIVE = (128, 128, 0)
MAROON = (128, 0, 0)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
NAVY = (0, 0, 128)
AQUA = (0, 255, 255)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

DISPLAY_WIDTH = 1240
DISPLAY_HEIGHT = 720
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

RECTANGLE_SIZE = 200
RECT_MID_200 = (DISPLAY_WIDTH / 2 - RECTANGLE_SIZE / 2, DISPLAY_HEIGHT / 2 - RECTANGLE_SIZE / 2, RECTANGLE_SIZE, RECTANGLE_SIZE)

# FUNCTIONS ------------------------------------------------------------------------------------------------ FUNCTIONS
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

while True:
	event_handler()
	
	# draw a rectangle in the center of the display surface using a predefined color
	pygame.draw.rect(DS, ORANGE, RECT_MID_200, 0)
	
	pygame.draw.rect(DS, (255, 165, 0), RECT_MID_200, 0)
	
	# update the display surface so we can see the changes
	pygame.display.update()