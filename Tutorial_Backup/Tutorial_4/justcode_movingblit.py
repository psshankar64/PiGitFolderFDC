''' This script loads an image and then moves it from left to right alternatively across the primary display surface

It's important to note that x, y represents the top left most position in your image. see diagram below

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

''' SETUP VARIABLES ------------------------------------------------------------------------------ SETUP VARIABLES '''
# determine which why the image is travelling, 1 = right, -1 = left
direction = 1

# starting position is the centre of the display surface
x = DW_HALF - R.center[0] # .center[0] = half image width, .center[1] = half image height


''' FUNCTIONS AND CLASSES ------------------------------------------------------------------------ FUNCTIONS AND CLASSES '''
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

			
''' MAIN LOOP ------------------------------------------------------------------------------------ MAIN LOOP '''
while True:
	event_handler()

	# draw the image in the center of the primary display surface (DS)
	DS.blit(MY_IMAGE, (x, DH_HALF - R.center[1]))
	
	# increment or deincrement the x position using the direction vector
	# direction vector could be 1 or -1
	x += direction
	
	# check if the image has reached either side of the display surface
	if x >= DISPLAY_WIDTH - R.width or x <= 0:
		direction *= -1 # swap the direction vector. -1 becomes 1, 1 becomes -1		
	
	pygame.display.update()
	
	# it's important in the this script to clear the display surface after updating
	# overwise you'll see a trail of images as it moves from one side of the display
	# surface to the other. Try deleting the line below and running the script again!
	DS.fill([0,0,0])
	
	
	
	
	
	
	
	