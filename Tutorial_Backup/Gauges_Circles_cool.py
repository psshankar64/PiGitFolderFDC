'''
This script loads an images and rotates it in the center of the display surface
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
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 480
DW_HALF = DISPLAY_WIDTH // 2
DH_HALF = DISPLAY_HEIGHT // 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

''' LOAD IMAGES ---------------------------------------------------------------------------------- LOAD IMAGES '''
Logo = pygame.image.load('./images/design.png')
coolCircle_org = pygame.image.load('./images/circle4.jpg')
#Logo = pygame.transform.rotate(Logo_org, 90)
Needle = pygame.image.load('./images/needle.png')
Gauge = pygame.image.load('./images/cadran.png')

smalllogo = pygame.transform.scale(Logo, (220,200))
coolCircle = pygame.transform.scale(coolCircle_org, (260,260))
''' FUNCTIONS ------------------------------------------------------------------------------------ FUNCTIONS '''
def event_handler():
        for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()

			
def rotate_and_center(ds, x, y, image, degrees):
# this function rotates an image and then centralises so that the rotation is uniform
	# rotate the object n degrees and store in a new surface called 'rotated'
        rotated = pygame.transform.rotate(image, degrees)
	
	# get the dimensions of the newly rotated image.
	# rect will contain width, height, horizontal center, vertical center
        rect = rotated.get_rect()
	
	# display the rotated image to the display surface
	# deduct horizontal and vertical center values from x and y to centralise the image
	# for example if the x value is 640 and the image is 50 pixels wide, then to centralise 
	# the image we must deduct 25 from 640
	
	#                             640
	#                              |
	# *****************|<----25---------25---->|*****************
        DS.blit(rotated, (x - rect.center[0], y - rect.center[1]))
	
	
	
''' SETUP VARIABLES ------------------------------------------------------------------------------ SETUP VARIABLES '''
# set the starting rotation of the image in degrees 
direction = 1;
degrees = 90;

''' MAIN LOOP ------------------------------------------------------------------------------------ MAIN LOOP '''			
while True:
        event_handler()

        DS.blit(smalllogo, (DW_HALF - 110, DH_HALF - 215))        
        #pygame.draw.circle(DS, (0,0,230), (DW_HALF - 220, DH_HALF - 10), 120, 45)
        #pygame.draw.circle(DS, (0,0,230), (DW_HALF + 220, DH_HALF - 10), 120, 45)
        #pygame.draw.circle(DS, (0,0,120), (DW_HALF - 220, DH_HALF + 30), 135, 25)
        #pygame.draw.circle(DS, (0,0,120), (DW_HALF + 220, DH_HALF + 30), 135, 25)
        #pygame.draw.rect(DS, (0, 0, 0), (DW_HALF - 355, DH_HALF + 50, 710, 140), 0)
        
        
	#Place the Gauge first and then show the needle)
        RECT = Gauge.get_rect()
        DS.blit(coolCircle, (DW_HALF - 223 - RECT.center[0], DH_HALF + 30 - RECT.center[1]))
        DS.blit(coolCircle, (DW_HALF + 217 - RECT.center[0], DH_HALF + 30 - RECT.center[1]))
        pygame.draw.rect(DS, (0, 0, 0), (DW_HALF - 355, DH_HALF + 40, 710, 140), 0)
        
	# rotate the image around 360 degrees but centralise it to x and y
        DS.blit(Gauge, (DW_HALF - 220 - RECT.center[0], DH_HALF + 30 - RECT.center[1]))
        rotate_and_center(DS, DW_HALF - 220, DH_HALF + 30, Needle, degrees)

        DS.blit(Gauge, (DW_HALF + 220 - RECT.center[0], DH_HALF + 30 - RECT.center[1]))
        rotate_and_center(DS, DW_HALF + 220, DH_HALF + 30, Needle, degrees)

	# increment the rotation. reset rotation if degrees is greater than 359 (not necessary but cleaner IMO)

        if degrees == 90:
                direction = 1
        elif degrees == -90:
                direction = 0

        if direction == 1:
                degrees -= 1
        elif direction == 0:
                degrees += 1


                
        CLOCK.tick(60) # *** NOT COVERED IN THE VIDEO ***
			
        pygame.display.update()
        DS.fill([0,0,0])
	
	
	
	
	
	
	
	
