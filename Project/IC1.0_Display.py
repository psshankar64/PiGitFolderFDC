'''
This script loads an images and rotates it in the center of the display surface
'''

import sys
import random
import math
import time

import pygame
import pygame.gfxdraw
from pygame.locals import *

#Define some standard colors
BootUp = True
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
MenuNum = 1
MENULISTCOLOR = (64, 64, 64)


ListItemColor1 = WHITE
ListItemColor2 = GRAY
ListItemColor3 = GRAY
ListItemColor4 = GRAY
ListItemColor5 = GRAY
ListItemColor6 = GRAY

'''Goabls We should not use it but for experiments we still keep this'''
degrees = 149;
FUELX = 100;
FUELCOLOR = GREEN;
FUELPERCVALUE = 100;
SELECTED = 1;
MenuItemNumber = 1
itemTextSize = 25
itemSelectedSize = 35
popupind = 0

pygame.init()
CLOCK = pygame.time.Clock() # *** NOT COVERED IN THE VIDEO ***

''' DISPLAY SETUP -------------------------------------------------------------------------------- DISPLAY SETUP '''
DISPLAY_WIDTH = 940
DISPLAY_HEIGHT = 480
DW_HALF = DISPLAY_WIDTH // 2
DH_HALF = DISPLAY_HEIGHT // 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT), pygame.FULLSCREEN)

''' LOAD IMAGES ---------------------------------------------------------------------------------- LOAD IMAGES '''
Needle_org = pygame.image.load('./images/needle.png')
Gauge_org = pygame.image.load('./images/CGaugeBlk.png')
Circle_org = pygame.image.load('./images/circle2.jpg')
StartUp_org = pygame.image.load('./images/logo.png')
popupBg_org = pygame.image.load('./images/blackBg.png')
popupIcon_org = pygame.image.load('./images/popupIcon.png')


Gauge = pygame.transform.scale(Gauge_org, (640,460))
Needle = pygame.transform.scale(Needle_org, (260,460))
Circle = pygame.transform.scale(Circle_org, (340, 260))
StartUp = pygame.transform.scale(StartUp_org, (640, 460))
popupBg = pygame.transform.scale(popupBg_org, (240, 260))
popupIcon = pygame.transform.scale(popupIcon_org, (50, 40))


''' FUNCTIONS ------------------------------------------------------------------------------------ FUNCTIONS '''

def display_logo():
        global BootUp
        
        DS.blit(StartUp, (150, 30))
        pygame.display.update()
        time.sleep(10)
        BootUp = False

def displayPopup():
        mainDisplay()
        DS.blit(popupBg, (380, 100))
        display_text('Contact Workshop', DW_HALF+25, 150, 25)
        display_text('Main beam problem', DW_HALF+25, 300, 25)
        pygame.draw.rect(DS, WHITE, (380, 100, 240, 260), 2)
        DS.blit(popupIcon, (470, 190))
        pygame.display.update()
        time.sleep(5)		

def mainDisplay():

        global FUELCOLOR
			#Place the Gauge first (and any other fixed shapes)
        RECT = Gauge.get_rect()        
        DS.blit(Gauge, (DW_HALF - RECT.center[0] - 230, DH_HALF - RECT.center[1]))
        pygame.draw.rect(DS, WHITE, (DW_HALF + 190, 173, 110, 30), 1)
        #pygame.draw.arc(DS, RED, [DW_HALF - 230, DH_HALF,20,20], degrees, 270) #(screen, color, (x,y,width,height), start_angle, stop_angle, thickness)
        
        if(FUELPERCVALUE > 60):
                FUELCOLOR = RICHGREEN
                print("Checkpoint green")
        elif(FUELPERCVALUE < 60):
                if(FUELPERCVALUE > 30):
                        FUELCOLOR = RICHYELLOW
                        print("Checkpoint yellow")
                else:
                        FUELCOLOR = RICHRED
        pygame.draw.rect(DS, FUELCOLOR, (DW_HALF + 195, 178, FUELX, 20), 0) 
        pygame.draw.rect(DS, SILVER, (DW_HALF + 65, 235, 280, 210), 1)

        #Place all the fixed texts here
        display_text('RPM', DW_HALF+100, 50, 30)
        display_text('ODO', DW_HALF+280, 50, 30)
        display_text('x1000', DW_HALF+100, 135, 20)
        display_text('KM', DW_HALF+350, 135, 20)
        display_text('FUEL', DW_HALF+100, 190, 40)
        

        #and then show the changed position of the needle
        rotate_and_center(DS, DW_HALF - 230, DH_HALF, Needle, degrees)

	#The degrees as of now is the global variable 
        raw_value = float(((149 - degrees) * 28)/1000)

        display_text(str(round(raw_value, 2)), DW_HALF+100, 100, 60)
        display_text("123456", DW_HALF+270, 100, 50)

        ListItemColor1 = GRAY
        ListItemColor2 = GRAY
        ListItemColor3 = GRAY
        ListItemColor4 = GRAY
        ListItemColor5 = GRAY
        #ListItemColor6 = GRAY

        if(MenuItemNumber == 1):
                ListItemColor1 = WHITE

        if(MenuItemNumber == 2):
                ListItemColor2 = WHITE

        if(MenuItemNumber == 3):
                ListItemColor3 = WHITE

        if(MenuItemNumber == 4):
                ListItemColor4 = WHITE

        if(MenuItemNumber == 5):
                ListItemColor5 = WHITE

        #if(MenuItemNumber == 6):
                #ListItemColor6 = WHITE

        if MenuNum <= 1:
                pygame.draw.rect(DS, MENULISTCOLOR, (MenuStart_X - 14, MenuStart_Y + (Y_MenuSpace - 1)* (MenuItemNumber - 1), 278, 24), 0)
                             
                display_text_NC("**Settings**", MenuStart_X, MenuStart_Y - 40, 30, WHITE)

                display_text_NC("Date and time", MenuStart_X, MenuStart_Y, 25, ListItemColor1)
                display_text_NC("Avg Consumption", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 1), 25, ListItemColor2)
                display_text_NC("Speed Govern", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 2), 25, ListItemColor3)
                display_text_NC("Connectivity", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 3), 25, ListItemColor4)
                display_text_NC("Infotainment", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 4), 25, ListItemColor5)
                #display_text_NC("Menu item Six", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 5), 25, ListItemColor6)
                
                pygame.display.update(DW_HALF + 65, 235, 280, 210)

        if(MenuNum >= 2):
                pygame.draw.rect(DS, MENULISTCOLOR, (MenuStart_X - 14, MenuStart_Y + (Y_MenuSpace - 1)* (MenuItemNumber - 1), 278, 24), 0)
                     
                display_text_NC("**Maintenance**", MenuStart_X, MenuStart_Y - 40, 30, WHITE)

                display_text_NC("Engine oil", MenuStart_X, MenuStart_Y, 25, ListItemColor1)
                display_text_NC("Battery Check", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 1), 25, ListItemColor2)
                display_text_NC("Range Check", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 2), 25, ListItemColor3)
                display_text_NC("Notifications", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 3), 25, ListItemColor4)
                display_text_NC("Calibration", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 4), 25, ListItemColor5)
                #display_text_NC("Menu item Six", MenuStart_X, (MenuStart_Y + Y_MenuSpace * 5), 25, ListItemColor6)

                pygame.display.update(DW_HALF + 65, 235, 280, 210)

        if(popupind > 0):
                popupsurf = pygame.Surface(DISPLAY_WIDTH, DISPLAY_HEIGHT)
                popupsurf.fill((255,255,255))
                popupsurf.set_alpha(128)
                DS.blit(s, (0,0))
        

        #The tick in the bracket will tell the maximum frames per second. Lower number means slower speed. Its not a delay func
        CLOCK.tick(60)

def event_handler():
        global degrees
        global FUELX
        global FUELPERCVALUE
        global MenuNum
        global MenuItemNumber
        global popupind
        
        for event in pygame.event.get():
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
                        #pygame.quit()
                        #sys.exit()
                        #mainDisplay()
                        print("Quit")
                        
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_a):
                        #global degrees
                        degrees += 1
                        if degrees > 149:
                                degrees = 149

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_d):
                        #global degrees
                        degrees -= 1
                        if degrees < -149:
                                degrees = -149

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_4):
                        if(FUELX > 0):
                                FUELX -= 2
                                FUELPERCVALUE -= 2

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_6):
                        if(FUELX < 100):
                                FUELX += 2
                                FUELPERCVALUE += 2

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_RIGHT):
                        MenuNum += 1
                        if(MenuNum > 2):
                                MenuNum = 1

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_LEFT):
                        MenuNum -= 1
                        if(MenuNum < 1):
                                MenuNum = 2

                if (event.type == pygame.KEYDOWN and event.key == pygame.K_DOWN and MenuItemNumber < 5):
                        MenuItemNumber += 1
                        
                if (event.type == pygame.KEYDOWN and event.key == pygame.K_UP and MenuItemNumber > 1):
                        MenuItemNumber -= 1

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_z):
                        popupind = 1

                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_x):
                        popupind = 2
                        
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_c):
                        popupind = 3
                        
                if event.type == QUIT or (event.type == KEYDOWN and event.key == K_v):
                        popupind = 4
		
                if event.type==pygame.KEYDOWN and event.key==pygame.K_1:
                        displayPopup()
                        
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

def display_text_NC(text, x_cord, y_cord, size, ListItemColor):
        texttype = pygame.font.Font('Light.ttf', size)
        textSurf = texttype.render(text, 1, ListItemColor)
        textRect = textSurf.get_rect()
        textRect.topleft = (x_cord, y_cord)
        DS.blit(textSurf, textRect)

# Text Renderer
def text_format(message, textFont, textSize, textColor):
    newFont=pygame.font.Font(textFont, textSize)
    newText=newFont.render(message, 0, textColor)

    return newText
	
''' SETUP VARIABLES ------------------------------------------------------------------------------ SETUP VARIABLES '''
# set the starting rotation of the image in degrees 
direction = 1;
raw_value = degrees * 0.8
MenuStart_X = DW_HALF + 80
MenuStart_Y = 280
#Y_MenuSpace = 25
Y_MenuSpace = 35

''' MAIN LOOP ------------------------------------------------------------------------------------ MAIN LOOP '''
while True:

        while BootUp is True:
                display_logo()
                                
        #Event handling currently handles ESC or any other keypress. This is a polling mechanism
        event_handler()
		
        mainDisplay()        
			
        pygame.display.update() #pygame.display.flip() is another option
        DS.fill([0,0,0])
	
