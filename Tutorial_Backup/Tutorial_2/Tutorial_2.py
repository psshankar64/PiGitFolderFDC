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

''' NOT COVERED IN THE VIDEO '''
pygame.font.init() 
FONT = pygame.font.Font(None, 15)
''' YOU CAN LOOK NOW! '''

DISPLAY_WIDTH = 1280 # screen width in pixels
DISPLAY_HEIGHT = 720 # screen height in pixels
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2
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

''' THE FUNCTIONS BELOW AREN'T COVERED IN THE VIDEO '''
def draw_ruler():
	global DS
	for x in xrange(10, DISPLAY_WIDTH - 10, 10):
		if x % 50 == 0:
			pygame.draw.line(DS, (255, 0, 0), (x, 0),(x, 10), 1)
			text(x, 13, "{0}".format(x), 1)
		else:
			pygame.draw.line(DS, (255, 0, 0), (x, 0), (x, 5), 1)
	for y in xrange(10, DISPLAY_HEIGHT - 10, 10):
		if y % 50 == 0:
			pygame.draw.line(DS, (255, 0, 0), (0, y),(10, y), 1)
			text(13, y, "{0}".format(y), 2)
		else:
			pygame.draw.line(DS, (255, 0, 0), (0, y),(5, y), 1)

def draw_center_indicator():
	global DS
	pygame.draw.line(DS, (255, 0, 0), (DW_HALF, DH_HALF - 25), (DW_HALF, DH_HALF - 5), 1)
	pygame.draw.line(DS, (255, 0, 0), (DW_HALF, DH_HALF + 5), (DW_HALF, DH_HALF + 25), 1)
	pygame.draw.line(DS, (255, 0, 0), (DW_HALF - 25, DH_HALF), (DW_HALF - 5, DH_HALF), 1)
	pygame.draw.line(DS, (255, 0, 0), (DW_HALF + 5, DH_HALF), (DW_HALF + 25, DH_HALF), 1)

def draw_mouse_position():
	global DS
	x, y = pygame.mouse.get_pos()
	text(x, y - 15, "x: {0}, y: {1}".format(x, y), 1)
	
def text(x, y, t, c = 0):
	global DS, FONT
	text_image = FONT.render(t, 1, (255, 0, 0))
	if c == 1:
		r = text_image.get_rect()
		DS.blit(text_image, (x - r.width / 2, y))
	elif c == 2:
		r = text_image.get_rect()
		DS.blit(text_image, (x, y - r.height / 2))
	elif c == 3:
		r = text_image.get_rect()
		DS.blit(text_image, (x - r.width / 2, y - r.height / 2))
	else:
		DS.blit(text_image, (x, y))

TRI_POINTS = 3
HEX_POINTS = 6
OCT_POINTS = 8

pi2 = math.pi * 2
triangle = list([(DW_HALF + math.cos((pi2 / TRI_POINTS) * i) * 300, DH_HALF + math.sin((pi2 / TRI_POINTS) * i) * 300) for i in xrange(TRI_POINTS)])
hexagon = list([(DW_HALF + math.cos((pi2 / HEX_POINTS) * i) * 300, DH_HALF + math.sin((pi2 / HEX_POINTS) * i) * 300) for i in xrange(HEX_POINTS)])
octagon = list([(DW_HALF + math.cos((pi2 / OCT_POINTS) * i) * 300, DH_HALF + math.sin((pi2 / OCT_POINTS) * i) * 300) for i in xrange(OCT_POINTS)])
''' BACK TO NORMAL FROM HERE :) '''


# MAIN ----------------------------------------------------------------------------------------------------- MAIN

# the main program loop. this will loop forever
# others don't structure their programs like this however i do, it a personal choice.
while True:
	event_handler() # check for [esc] or window [x] pressed
	
	''' This draws a solid white (255, 255, 255) rectangle at location 0, 0 (top left) on our display surface (DS)
	with a width of half the display width and a height of half the display height '''
	pygame.draw.rect(DS, (255, 255, 255), (250, 250, DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2), 0)
	#pygame.draw.rect(DS, (255, 255, 255), (250, 250, DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2), 0)

	#pygame.draw.line(DS, (0, 0, 255), (250 + DW_HALF / 2, 250), (250 + DW_HALF / 2, 250 + DH_HALF), 1)
	#pygame.draw.line(DS, (0, 0, 255), (250, 250 + DH_HALF / 2), (250 + DW_HALF, 250 + DH_HALF / 2), 1)
	#pygame.draw.line(DS, (0, 0, 255), (0, 0), (1280, 720), 5)
	
	#pygame.draw.circle(DS, (255, 255, 255), (DISPLAY_WIDTH / 2, DISPLAY_HEIGHT / 2), 150, 1)
	
	#pygame.draw.polygon(DS, (255, 255, 255), triangle, 0)
	#pygame.draw.polygon(DS, (255, 255, 255), hexagon, 0)
	#pygame.draw.polygon(DS, (255, 255, 255), octagon, 0)
	
	# these functions draw ruler lines to indicate position
	draw_ruler()
	draw_center_indicator()
	draw_mouse_position()
	
	
	# update the screen. this is important as drawing graphics (square, lines, circles) won't appear until you have called update()
	pygame.display.update()
	
	# clear the surfuce to black.
	DS.fill([0,0,0])
	
	
	
	
	
	
	
	