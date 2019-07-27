import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()
pygame.font.init() 
FONT = pygame.font.Font(None, 30)

''' DISPLAY SETUP -------------------------------------------------------------------------------- DISPLAY SETUP '''
DISPLAY_WIDTH = 1240
DISPLAY_HEIGHT = 720
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

''' DATA TABLES ---------------------------------------------------------------------------------- DATA TABLE '''
D2R = (math.pi * 2) / 360
DIRECTION_VECTOR_LOOKUP = list([[math.cos(D2R * degrees), math.sin(D2R * degrees)] for degrees in xrange(360)])			
DIRECTION_VECTOR_LOOKUP[90][0] = 0
DIRECTION_VECTOR_LOOKUP[180][1] = 0
DIRECTION_VECTOR_LOOKUP[270][0] = 0

''' SETUP VARIABLES ------------------------------------------------------------------------------ SETUP VARIABLES '''
circle_x = 0.0 + DW_HALF
circle_y = 0.0 + DH_HALF
circle_move = False

''' FUNCTIONS ------------------------------------------------------------------------------------ FUNCTIONS '''
def event_handler():
	global circle_move
	
	for event in pygame.event.get():
		print event.type
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN and event.button == 1:
			circle_move = True
		elif event.type == MOUSEBUTTONUP and event.button == 1:
			circle_move = False			

''' MAIN LOOP ------------------------------------------------------------------------------------ MAIN LOOP '''
while True:
	event_handler()

	mx, my = pygame.mouse.get_pos()
	v = int(pygame.math.Vector2().angle_to((mx - DW_HALF, my - DH_HALF)))
	if v < 0:
		v = 360 - (v * -1)
	
	for i in xrange(360):
		if i == v:
			px = DW_HALF + DIRECTION_VECTOR_LOOKUP[i][0] * 320
			py = DH_HALF + DIRECTION_VECTOR_LOOKUP[i][1] * 320
			
			pygame.draw.line(DS, (255, 0, 255), (DW_HALF, DH_HALF), (px, py), 1)
			pygame.draw.circle(DS, (255, 0, 0), (int(px), int(py)), 10, 0)
			
		else:
			pygame.draw.line(
				DS,
				(255, 255, 255),
				(DW_HALF, DH_HALF),
				(DW_HALF + DIRECTION_VECTOR_LOOKUP[i][0] * 300, DH_HALF + DIRECTION_VECTOR_LOOKUP[i][1] * 300),
				1)
		
	text = "deg: {0}, dx: {1}, dy: {2}" . format(v, DIRECTION_VECTOR_LOOKUP[v][0], DIRECTION_VECTOR_LOOKUP[v][1])
	text_image = FONT.render(text, 1, (255, 255, 255))
	
	DS.blit(text_image, (DW_HALF - text_image.get_rect().width / 2, 690))
	
	if circle_move:
		circle_x += DIRECTION_VECTOR_LOOKUP[v][0]
		circle_y += DIRECTION_VECTOR_LOOKUP[v][1]
	
	pygame.draw.circle(DS, (0, 128, 0), (int(circle_x), int(circle_y)), 25, 0)
	
	pygame.display.update()

	DS.fill((0, 0, 0))
	
pygame.quit()