'''
This script loads an image containing a series of images which when displayed as an animation
showing a cat walking
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
# Load the image into the CAT container
CAT = pygame.image.load('catwalk.png')
# get the dimensions of the cat image
RECT = CAT.get_rect()

''' SETUP VARIABLES ------------------------------------------------------------------------------ SETUP VARIABLES '''
# the cat image is separated into 12 animation 'frames'. If the image was drawn to the display surface as it is on the
# harddisk then there would be any animation, the view would is all the frames at once. The trick is to display only a
# portion of the image. In the image the cats are stacked vertically so each frame only needs to reference a y offset
# to correspond to the frame number.
# So...
# frame 0 = (0, frame_height * 0, image.width, frame_height)
# frame 1 = (0, frame_height * 1, image.width, frame_height)
# frame 2 = (0, frame_height * 2, image.width, frame_height)
#
# remember the structure of a rectangle in pygame is (x, y, width, height)
#
# So instead of chopping the cat image into 12 pieces we are simply creating a list of places on the cat image
# where the frames are.
FRAME_COUNT = 12
FRAME_HEIGHT = RECT.height / FRAME_COUNT
FRAMES = list([(0, FRAME_HEIGHT * frame, RECT.width, FRAME_HEIGHT) for frame in xrange(FRAME_COUNT)])

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
	DS.blit(CAT, (DW_HALF - RECT.center[0], DH_HALF - FRAME_HEIGHT / 2), FRAMES[frame])
	
	# increment the frame count and if the frame count is greater than FRAME_COUNT - 1 then reset to 0
	frame += 1
	if frame > FRAME_COUNT - 1:
		frame = 0
		
	pygame.display.update()
	
	CLOCK.tick(5) # *** NOT COVERED IN THE VIDEO ***
	
	# because the cat in the animation is black, the background colour needs to be something other
	# than that. In this case it's grey
	DS.fill((128, 128, 128))