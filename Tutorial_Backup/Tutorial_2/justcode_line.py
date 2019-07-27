

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

DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 600
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# FUNCTIONS ------------------------------------------------------------------------------------------------ FUNCTIONS
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

PI = math.pi # simplifies the code
rotation = 0.0 # create a floating point number for the line rotation
rotation_vector = (PI * 2) / 360 # the line will rotate through 360 degrees
rotation_radius = 250 # how big the rotation 'circle' radius is

while True:
	event_handler()
	
	# starting co-ordinates of the line
	x1 = DW_HALF + math.cos(rotation) * rotation_radius
	y1 = DH_HALF + math.sin(rotation) * rotation_radius
	
	
	# ending co-ordinates of the line
	x2 = DW_HALF + math.cos(rotation + PI) * rotation_radius
	y2 = DH_HALF + math.sin(rotation + PI) * rotation_radius
	
	# increase rotation by 1 degree
	rotation += rotation_vector
	
	
	# draw a blue line on the primary display surface starting at x1,y1 and ending at x2, y2 with a thickness of 5pixels
	pygame.draw.line(DS, BLUE, (x1, y1), (x2, y2), 5)
	
	pygame.display.update()
	DS.fill([0,0,0])