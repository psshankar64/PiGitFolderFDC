import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *

''' It maybe important to point out that i use CAPS to show a constant variable, ie has the same value all the way through the program. '''
''' This is personal choice and others may not use this distinction '''

# initialise the pygame library
pygame.init()

DISPLAY_WIDTH = 800 # screen width in pixels
DISPLAY_HEIGHT = 600 # screen height in pixels
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT # screen area in pixels

# create the primary display surface (DS) based on our chosen resolution
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

# FUNCTIONS ------------------------------------------------------------------------------------------------ FUNCTIONS

# this function handles window controls [x] and key presses [esc].
def event_handler():
	for event in pygame.event.get():
		# if [esc] or [x] pressed...
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			# ... then quit!
			pygame.quit()
			sys.exit() 
		
# MAIN ----------------------------------------------------------------------------------------------------- MAIN

# the main program loop. this will loop forever
# others don't structure their programs like this however i do, it a personal choice.
while True:
	event_handler() # check for [esc] or window [x] pressed
	
	# update the screen. this is important as drawing graphics (square, lines, circles) won't appear until you have called update()
	pygame.display.update()
	
	# clear the surfuce to black.
	DS.fill([0,0,0])