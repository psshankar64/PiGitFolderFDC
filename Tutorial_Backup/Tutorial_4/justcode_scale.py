''' This scripts loads an image and then scales it up and down '''

import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()
CLOCK = pygame.time.Clock() # *** NOT COVERED IN THE VIDEO ***


''' DISPLAY SETUP -------------------------------------------------------------------------------- DISPLAY SETUP '''
DISPLAY_WIDTH = 1240
DISPLAY_HEIGHT = 720
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

''' LOAD IMAGES ---------------------------------------------------------------------------------- LOAD IMAGES '''
# load the colorwheel image into the BALL container
BALL = pygame.image.load('colorwheel_100.png')
RECT = BALL.get_rect() # get the rectangle dimension of the image (100x100)

# FUNCTIONS ------------------------------------------------------------------------------------------------ FUNCTIONS
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

''' SETUP VARIABLES ------------------------------------------------------------------------------ SETUP VARIABLES '''
MAX_SCALE = 200 # this sets the maximum size (in pixels) the ball image will be scaled to
MIN_SCALE = 10 # the minimum size
current_scale = MIN_SCALE # the starting scale of the ball
scale_direction = 1 # the direction the scale will go in, 1 = increase size, -1 is decrease size

while True:
	event_handler()

	# create a new image consisting of the ball scaled up or down
	scaled = pygame.transform.scale(BALL, (current_scale, current_scale))
	
	# because we've just scaled the ball image the dimensions of it have now changed and if we
	# want to centralise the image on the x, y coordinates then we need to know the new .center[0]
	# and .center[1] values
	new_rect = scaled.get_rect()
	
	# draw the newly scaled ball centered to the display surface (DS)
	DS.blit(scaled, (DW_HALF - new_rect.center[0], DH_HALF - new_rect.center[1]))
	
	# increment or decrement the current scale value. scale_direction will be either 1 or -1
	current_scale += scale_direction
	# check if the current_scale has reached our bounderies and if true then set the scale direction
	# to the opposite of what it currently is. 1 = -1, -1 = 1
	if current_scale == MAX_SCALE or current_scale == MIN_SCALE:
		scale_direction = -scale_direction
			
	# update the display surface
	pygame.display.update()
	
	CLOCK.tick(30) # *** NOT COVERED IN THE VIDEO ***	
	
	# clear the display surface to black
	DS.fill((0,0,0))