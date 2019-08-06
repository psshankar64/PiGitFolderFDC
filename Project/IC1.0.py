'''
This script loads an images and rotates it in the center of the display surface
'''

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
RICHGREEN = (81, 225, 115)
OLIVE = (128, 128, 0)
YELLOW = (255, 255, 0)
RICHYELLOW = (211, 216, 66)
ORANGE = (255, 165, 0)
RED = (255, 0, 0)
RICHRED = (229, 20, 20)
MAROON = (128, 0, 0)
SILVER = (192, 192, 192)
GRAY = (128, 128, 128)
BLUE = (0, 0, 255)
NAVY = (0, 0, 128)
AQUA = (0, 255, 255)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

'''Goabls We should not use it but for experiments we still keep this'''
degrees = 145;
FUELX = 100;
FUELCOLOR = GREEN;
FUELPERCVALUE = 100;
SELECTED = 1;

pygame.init()
CLOCK = pygame.time.Clock() # *** NOT COVERED IN THE VIDEO ***

''' DISPLAY SETUP -------------------------------------------------------------------------------- DISPLAY SETUP '''
DISPLAY_WIDTH = 800
DISPLAY_HEIGHT = 480
DW_HALF = DISPLAY_WIDTH // 2
DH_HALF = DISPLAY_HEIGHT // 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), pygame.NOFRAME)

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
        global FUELX
        global FUELPERCVALUE
        
        for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        pygame.quit()
                        sys.exit()
                        
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_LEFT):
                        #global degrees
                        degrees += 1
                        if degrees > 145:
                                degrees = 145

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_RIGHT):
                        #global degrees
                        degrees -= 1
                        if degrees < -145:
                                degrees = -145

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_4):
                        if(FUELX > 0):
                                FUELX -= 10
                                FUELPERCVALUE -= 10

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_6):
                        if(FUELX < 100):
                                FUELX += 10
                                FUELPERCVALUE += 10
                                
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
	

def display_text(text, x_cord, y_cord, size):
        texttype = pygame.font.Font('Light.ttf', size)
        textSurf = texttype.render(text, 1, (255, 255, 255))
        textRect = textSurf.get_rect()
        textRect.center = (x_cord, y_cord)
        DS.blit(textSurf, textRect)
        return textSurf

def display_text_NC(text, x_cord, y_cord, size):
        texttype = pygame.font.Font('Light.ttf', size)
        textSurf = texttype.render(text, 1, (255, 255, 255))
        textRect = textSurf.get_rect()
        textRect.topleft = (x_cord, y_cord)
        DS.blit(textSurf, textRect)  
	
''' SETUP VARIABLES ------------------------------------------------------------------------------ SETUP VARIABLES '''
# set the starting rotation of the image in degrees 
direction = 1;
raw_value = degrees * 0.8
MenuStart_X = DW_HALF + 80
MenuStart_Y = 260
Y_MenuSpace = 25

''' MAIN LOOP ------------------------------------------------------------------------------------ MAIN LOOP '''
while True:
        #Event handling currently handles ESC or any other keypress. This is a polling mechanism
        event_handler()

        #Place the Gauge first (and any other fixed shapes)
        RECT = Gauge.get_rect()        
        DS.blit(Gauge, (DW_HALF - RECT.center[0] - 170, DH_HALF - RECT.center[1]))
        pygame.draw.rect(DS, WHITE, (DW_HALF + 190, 173, 110, 30), 1)
        if(FUELPERCVALUE > 60):
                FUELCOLOR = RICHGREEN
        elif(FUELPERCVALUE < 60):
                if(FUELPERCVALUE > 30):
                        FUELCOLOR = RICHYELLOW
                else:
                        FUELCOLOR = RICHRED
        pygame.draw.rect(DS, FUELCOLOR, (DW_HALF + 195, 178, FUELX, 20), 0) 
        pygame.draw.rect(DS, SILVER, (DW_HALF + 65, 235, 280, 220), 5)

        #Place all the fixed texts here
        display_text('RPM', DW_HALF+100, 50, 30)
        display_text('ODO', DW_HALF+280, 50, 30)
        display_text('x1000', DW_HALF+100, 135, 20)
        display_text('KM', DW_HALF+350, 135, 20)
        display_text('FUEL', DW_HALF+100, 190, 40)
        

        #and then show the changed position of the needle
        rotate_and_center(DS, DW_HALF - 170, DH_HALF, Needle, degrees)

	#The degrees as of now is the global variable 
        raw_value = float(((145 - degrees) * 28)/1000)

        display_text(str(round(raw_value, 2)), DW_HALF+100, 100, 60)
        display_text("123456", DW_HALF+270, 100, 50)

        display_text_NC("Menu item One", MenuStart_X, MenuStart_Y, 25)
        display_text_NC("Menu item Two", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 1), 25)
        display_text_NC("Menu item Three", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 2), 25)
        display_text_NC("Menu item Four", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 3), 25)
        display_text_NC("Menu item Five", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 4), 25)
        display_text_NC("Menu item Six", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 5), 25)

        #The tick in the bracket will tell the maximum frames per second. Lower number means slower speed. Its not a delay func
        CLOCK.tick(60) 
			
        pygame.display.update() #pygame.display.flip() is another option
        DS.fill([0,0,0])
	
	
	
	
	
	
	
	
