'''
This script loads an images and rotates it in the center of the display surface
'''

import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *

'''Goabls We should not use it but for experiments we still keep this'''
degrees = 140;

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
Needle_org = pygame.image.load('./images/needle.png')
Gauge = pygame.image.load('./images/CGaugeBlk.png')
Circle_org = pygame.image.load('./images/circle2.jpg')


#Gauge = pygame.transform.scale(Gauge_org, (340,260))
Needle = pygame.transform.scale(Needle_org, (260,360))
Circle = pygame.transform.scale(Circle_org, (340, 260))
''' FUNCTIONS ------------------------------------------------------------------------------------ FUNCTIONS '''
def event_handler():
        global degrees
        for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                        
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_DOWN):
                        #global degrees
                        degrees += 1
                        if degrees > 140:
                                degrees = 140

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_UP):
                        #global degrees
                        degrees -= 1
                        if degrees < -140:
                                degrees = -140

			
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
        DS.blit(rotated, (x - rect.center[0] + 8, y - rect.center[1] + 10))
	

def display_text(text, x_cord, y_cord):
        texttype = pygame.font.Font('Light.ttf', 25)
        textSurf = texttype.render(text, 1, (255, 255, 255))
        textRect = textSurf.get_rect()
        textRect.center = (x_cord, y_cord)
        DS.blit(textSurf, textRect)
        pygame.display.flip()
        
        
	
''' SETUP VARIABLES ------------------------------------------------------------------------------ SETUP VARIABLES '''
# set the starting rotation of the image in degrees 
direction = 1;
raw_value = degrees * 0.8

''' MAIN LOOP ------------------------------------------------------------------------------------ MAIN LOOP '''			
while True:
        event_handler()

        #Place the Gauge first and then show the needle)
        RECT = Gauge.get_rect()
        DS.blit(Gauge, (DW_HALF - RECT.center[0] - 170, DH_HALF - RECT.center[1]))
        rotate_and_center(DS, DW_HALF - 170, DH_HALF, Needle, degrees)

	# increment the rotation. reset rotation if degrees is greater than 359 (not necessary but cleaner IMO)

        '''if degrees == 140:
                direction = 1
        elif degrees == -140:
                direction = 0

        if direction == 1:
                degrees -= 1
        elif direction == 0:
                degrees += 1'''

        raw_value = int(degrees * 0.8)

        display_text(str(raw_value), DW_HALF+190, 150)
                
        CLOCK.tick(60) # *** NOT COVERED IN THE VIDEO ***
			
        pygame.display.update()
        DS.fill([0,0,0])
	
	
	
	
	
	
	
	
