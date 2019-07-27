import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()
pygame.font.init() 
FONT = pygame.font.Font(None, 30)

DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT

DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

RECT_SIZE = 100
parameters = list(
	[
		[0, 255, 255], [0, 255, 255], [0, 255, 255],
		[0, DISPLAY_WIDTH, DW_HALF - RECT_SIZE / 2], [0, DISPLAY_HEIGHT, DH_HALF - RECT_SIZE / 2],
		[-DISPLAY_WIDTH, DISPLAY_WIDTH, RECT_SIZE], [-DISPLAY_HEIGHT, DISPLAY_HEIGHT, RECT_SIZE],
		[0, 1, 0],
	])

CODE = "pygame.draw.rect(DS, ({0:03d}, {1:03d}, {2:03d}), ({3:03d}, {4:03d}, {5:03d}, {6:03d}), {7})"
CODE_X = 50
CODE_Y = DISPLAY_HEIGHT - 50
HOTSPOTS = list(
	[
		[220, 262, "Red", 0],
		[274, 306, "Green", 1],
		[318, 352, "Blue", 2],
		[378, 410, "X", 3],
		[422, 456, "Y", 4],
		[465, 500, "Width", 5],
		[510, 546, "Height", 6],
		[556, 580, "Fill?", 7],
	])
LABEL_Y = CODE_Y + 25

mouse_wheel_status = 0

# FUNCTIONS ------------------------------------------------------------------------------------------------ FUNCTIONS
def event_handler():
	global mouse_wheel_status
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONDOWN or event.type == MOUSEBUTTONUP:
			b = event.button
			if b > 3 and b < 6:
				mouse_wheel_status = b - 3
			
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

def draw_rect(p = parameters):
	global DS
	
	pygame.draw.rect(DS, (p[0][2], p[1][2], p[2][2]), (p[3][2], p[4][2], p[5][2], p[6][2]), p[7][2])
	
def draw_code(p = parameters):
	global DS
	global CODE_X, CODE_Y, CODE
	
	text(CODE_X, CODE_Y, CODE.format(p[0][2], p[1][2], p[2][2], p[3][2], p[4][2], p[5][2], p[6][2], p[7][2]), 0)

def check_hotspot(hs = HOTSPOTS, p = parameters):
	global CODE_X, LABEL_Y
	global mouse_wheel_status
	mx, my = pygame.mouse.get_pos()
	for h in hs:
		x1 = h[0] + CODE_X
		x2 = h[1] + CODE_X
		
		if mx >= x1 and mx <= x2:
			text(mx, LABEL_Y, h[2], 1)
			if mouse_wheel_status != 0:
				if mouse_wheel_status == 1:
					p[h[3]][2] -= 5
					if p[h[3]][2] < p[h[3]][0]:
						p[h[3]][2] = p[h[3]][0]
				if mouse_wheel_status == 2:
					p[h[3]][2] += 5
					if p[h[3]][2] > p[h[3]][1]:
						p[h[3]][2] = p[h[3]][1]
				mouse_wheel_status = 0

# MAIN ----------------------------------------------------------------------------------------------------- MAIN			
while True:
	event_handler()
	
	text(DW_HALF, 25, "Use the mouse wheel to change the value in the code below", 1)
	draw_rect()
	draw_code()
	check_hotspot()
	
	pygame.display.update()
	DS.fill([0,0,0])