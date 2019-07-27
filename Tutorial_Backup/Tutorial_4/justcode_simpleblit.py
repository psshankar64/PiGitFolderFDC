''' This script loads an image and then draws it in the centre of the primary display surface

it's important to note that x, y represents the top left most position in your image. see diagram below

		   y
		   |
		x -@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		   @@@@@@@@@ @@@@@@@@@@@@ @@@@@@@@@
		   @@@@@@@@   @@@@@@@@@@   @@@@@@@@
		   @@@@@@@@  @@@@@@@@@@@@  @@@@@@@@
		   @@@@@@@@  @@@@@@@@@@@@  @@@@@@@@
		   @@@@@@@@  @@@@@@@@@@@@  @@@@@@@@
		   @@@@@@@@   @@@@@@@@@@   @@@@@@@@
		   @@@@@@@@@ @@@@@@@@@@@@ @@@@@@@@@
		   @@@  @@@@@@@@@@@@@@@@@@@@@@  @@@
		   @@@@                        @@@@
		   @@@@@@@@@@            @@@@@@@@@@
		   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
		   @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@- width
										  |
										height
This means that if you'd like to centralise your image on x, y
you need to subtract half the width and half the height of your image for x, and yield

for example:
	displaysurface.blit(image, (x - image_width / 2, y - image_height / 2)
	
'''
import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

''' DISPLAY SETUP -------------------------------------------------------------------------------- DISPLAY SETUP '''
DISPLAY_WIDTH = 1240
DISPLAY_HEIGHT = 720
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

''' LOAD IMAGES ---------------------------------------------------------------------------------- LOAD IMAGES '''
# Load the image from a file
# Supported formats are JPEG, PNG, GIF
MY_IMAGE = pygame.image.load('colorwheel_100.png')

# Get the dimensions of the image by calling the Surface get_rect() function
R = MY_IMAGE.get_rect()

# display dimension information about the image loaded. This can be seen in the console window
print R

''' FUNCTIONS ------------------------------------------------------------------------------------ FUNCTIONS '''
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

			
''' MAIN LOOP ------------------------------------------------------------------------------------ MAIN LOOP '''
while True:
	event_handler()

	# draw the image in the center of the primary display surface (DS)
	DS.blit(MY_IMAGE, (DW_HALF - R.center[0], DH_HALF - R.center[1]))
	
	pygame.display.update()
	DS.fill((0,0,0))
	
	
	
	
	
	
	
	
	
	
	
	