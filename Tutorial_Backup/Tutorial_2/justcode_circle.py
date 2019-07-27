# This script will demonstrate how to draw a rectangle

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
GREEN = (0, 255, 0)
OLIVE = (128, 128, 0)
YELLOW = (255, 255, 0)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
MAROON = (128, 0, 0)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
NAVY = (0, 0, 128)
AQUA = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

pygame.init()

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# FUNCTIONS ------------------------------------------------------------------------------------------------ FUNCTIONS
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

while True:
	event_handler()
	
	# draw a solid green circle at x:0 y:0 (top left corner) with a radius of 100 pixels
	pygame.draw.circle(DS, GREEN, (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2), 150, 0)    #PY 3 will always return a float so we need to put in the // to get integer
	
	# draw a hollow red circle in the center of the display surface
	pygame.draw.circle(DS, RED, (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2), 120, 0)

	pygame.draw.circle(DS, GREEN, (DISPLAY_WIDTH // 2, DISPLAY_HEIGHT // 2), 50, 0)
	
	pygame.display.update()
	DS.fill([0,0,0])
