'''
This script loads a series of images which when displayed as an animation shows a cat walking
'''
import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

CLOCK = pygame.time.Clock() # *** NOT COVERED IN THE VIDEO ***

''' DISPLAY SETUP -------------------------------------------------------------------------------- DISPLAY SETUP '''
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

''' LOAD IMAGES ---------------------------------------------------------------------------------- LOAD IMAGES '''
# Load the squence images into a list. We load the image by changing the filename, each filename has
# a number at the end to specify the frame number. In the code below {0} is replaced by a number generated
# by the for loop 1 - 12 (13 is never reached)
CATS = list([pygame.image.load('catwalk_{0}.png'.format(i)) for i in xrange(1, 13)])

# So now the list should look like this
#		CATS[0] is catwalk_1.png
#		CATS[1] is catwalk_2.png
#		CATS[2] is catwalk_3.png
#		CATS[3] is catwalk_4.png
# 		...

# because all the images in the list are the same size we can use the first image in the list to get the dimensions
RECT = CATS[0].get_rect()

''' SETUP VARIABLES ------------------------------------------------------------------------------ SETUP VARIABLES '''
FRAME_COUNT = 12

''' FUNCTIONS AND CLASSES ------------------------------------------------------------------------ FUNCTIONS AND CLASSES '''
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

''' SETUP SOME MORE VARIABLES -------------------------------------------------------------------- SETUP SOME MORE VARIABLES '''
# the starting frame of the animation
frame = 0

''' MAIN LOOP ------------------------------------------------------------------------------------ MAIN LOOP '''
while True:
	event_handler()

	# draw the portion of the cat image that relates to the frame we wish to display
	# remember FRAMES is a list of offsets in the form of a rectangle (x, y, width, height)
	DS.blit(CATS[frame], (DW_HALF - RECT.center[0], DH_HALF - RECT.center[1]))
	
	# increment the frame count and if the frame count is greater than FRAME_COUNT - 1 then reset to 0
	frame += 1
	if frame > FRAME_COUNT - 1:
		frame = 0
		
	pygame.display.update()
	
	CLOCK.tick(5) # *** NOT COVERED IN THE VIDEO ***
	
	# because the cat in the animation is black, the background colour needs to be something other
	# than that. In this case it's grey
	DS.fill((128, 128, 128))