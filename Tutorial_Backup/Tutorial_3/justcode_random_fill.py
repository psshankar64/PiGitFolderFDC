# This script will fill the display surface a random color
# WARNING: if you suffer from photo-sensitive epilepsy then I'd not recommend running this script!

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

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
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
	
	# create the random color (R, G, B), remember red, green and blue values are 0-255, 0 = DARKEST, 255 = BRIGHTEST
	rgb = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
	
	# fill the display surface with the choosen color
	DS.fill(rgb)
	
	# update the display surface so we can see the changes
	pygame.display.update()