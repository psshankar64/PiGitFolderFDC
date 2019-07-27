'''
This script allows you to dynamically change the value Red Green and Blue values of a circle using the slider bars.
Click on an orbiting circle to copy the center circle color to it.
'''

import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *


# CLASSES -------------------------------------------------------------------------------------------------- CLASSES

class interactive_area:
	x1, y1, x2, y2, mask, bkgd = -1, -1, -1, -1, -1, -1
	def __init__(self, x, y, m, background_color = (0, 0, 0, 255)):
		r = m.get_rect()
		self.x1, self.y1, self.x2, self.y2 = x, y, x + r.width,  y + r.height
		self.mask, self.bkgd = m, background_color
		
	def test(self, x, y):
		if x >= self.x1 and y >= self.y1 and x <= self.x2 and y <= self.y2:
			ox, oy = x - self.x1, y - self.y1
			try:
				mask_col = self.mask.get_at((ox, oy))
			except:
				return (False, -1, -1)
			if  mask_col != self.bkgd:
				return (True, ox, oy)
		return (False, -1, -1)		

class orbital:
	color = (255, 255, 255)
	def __init__(self, x, y, s):
		mask = pygame.Surface((s * 2, s * 2))
		pygame.draw.circle(mask, (255, 255, 255), (s, s), s, 0)
		self.ia = interactive_area(x - s, y - s, mask)
		self.x = x
		self.y = y
		self.s = s
	
	def set_color(self, c):
		self.color = c
	
	def draw(self, display):
		pygame.draw.circle(display, self.color, (self.x, self.y), self.s, 0)

class slider:
	value = 128
	def __init__(self, x, y, w, h, min, max, label, label_color, label_pos):
		mask = pygame.Surface((w, h))
		mask.fill((255, 255, 255))
		self.ia = interactive_area(x, y, mask)
		
		self.x, self.y, self.w, self.h, self.min, self.max = x, y, w, h, min, max
		self.label, self.label_color, self.label_pos = label, label_color, label_pos
		self.vector = h / max - min
		self.widget_size = h / self.vector
	
	def set_value(self, y):
		self.value = y / self.vector
		
	def draw(self, display):
		global FONT
		ext = self.w / 2
		
		pygame.draw.rect(display, (128, 128, 128), (self.x, self.y - ext, self.w, self.h + (ext * 2)), 0)
		pygame.draw.rect(display, (255, 255, 255), (self.x, self.y, self.w, self.h), 0)
		pygame.draw.rect(display, (128, 0, 0), (self.x, self.y + self.value - ext, self.w, self.vector + 1 + (ext * 2)), 0)
		text_image = FONT.render("{0}".format(self.value), 1, (0, 0, 255))
		display.blit(text_image, ((self.x + self.w / 2) - text_image.get_rect().width / 2, self.y - ext + 1))
		
		label_image = FONT.render(self.label, 1, self.label_color)
		label_x_pos = (self.x + self.w / 2) - (label_image.get_rect().width / 2)
		if self.label_pos == 1:
			label_y_pos = (self.y + self.h + ext + 5)
		else:
			label_y_pos = (self.y - ext - label_image.get_rect().height - 5)			
		display.blit(label_image, (label_x_pos, label_y_pos))
		
		
# INITIALISATION AND GLOBAL VARIABLES ---------------------------------------------------------------------- INITIALISATION AND GLOBAL VARIABLES
pygame.init()
pygame.font.init() 
FONT = pygame.font.Font(None, 15)

DISPLAY_WIDTH = 1280
DW_HALF = DISPLAY_WIDTH / 2
DISPLAY_HEIGHT = 720
DH_HALF = DISPLAY_HEIGHT / 2

DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT

DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

PI2 = math.pi * 2

COMMON_SIZE_FACTOR = DH_HALF / 6
CENTER_SIZE = DH_HALF / 2 - (COMMON_SIZE_FACTOR / 2)
CENTER_POSITION_XY = (DW_HALF + DW_HALF / 2, DH_HALF)


ORBITAL_SIZE = COMMON_SIZE_FACTOR
ORBITAL_DISTANCE_FROM_CENTER = CENTER_SIZE + ORBITAL_SIZE / 2
NUMBER_OF_ORBITALS = 6
ORBITAL_SPACING_VECTOR = PI2 / NUMBER_OF_ORBITALS
ORBITALS = list([orbital(
	int(math.floor(CENTER_POSITION_XY[0] + math.cos(ORBITAL_SPACING_VECTOR * n) * ORBITAL_DISTANCE_FROM_CENTER)),
	int(math.floor(CENTER_POSITION_XY[1] + math.sin(ORBITAL_SPACING_VECTOR * n) * ORBITAL_DISTANCE_FROM_CENTER)),
	ORBITAL_SIZE
	) for n in xrange(NUMBER_OF_ORBITALS)])

SLIDER_WIDTH = 25
SLIDER_HEIGHT = 256
SLIDER_SPACING = 40
SLIDER_Y = DH_HALF - (SLIDER_HEIGHT / 2 - SLIDER_WIDTH / 2)
SLIDER_X = 40 #DW_HALF / 2 - (SLIDER_WIDTH * 3 + SLIDER_SPACING * 2) / 2
SLIDERS = list([
	slider(SLIDER_X, SLIDER_Y, SLIDER_WIDTH, 256, 0, 255, "red", (255, 0, 0), 0),
	slider(SLIDER_X + (SLIDER_WIDTH + SLIDER_SPACING), SLIDER_Y, SLIDER_WIDTH, 256, 0, 255, "green", (0, 255, 0), 1),
	slider(SLIDER_X + (SLIDER_WIDTH * 2 + SLIDER_SPACING * 2), SLIDER_Y, SLIDER_WIDTH, 256, 0, 255, "blue", (0, 0, 255), 0)
	])

MIXER_WIDTH = 150
MIXER_HEIGHT = 150
MIXER_X = 90 + (SLIDER_WIDTH * 3 + SLIDER_SPACING * 2)
MIXER_Y = DH_HALF - MIXER_HEIGHT / 2

# FUNCTIONS ------------------------------------------------------------------------------------------------ FUNCTIONS
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()
		elif event.type == MOUSEBUTTONUP and event.button == 1:
			# check if user has clicked and interactive area
			check_ias()
			
def check_ias():
	global SLIDERS
	mx, my = pygame.mouse.get_pos()
	for s in SLIDERS:
		hit = s.ia.test(mx, my)
		if hit[0]:
			s.set_value(hit[2])
			return
			
	for o in ORBITALS:
		hit = o.ia.test(mx, my)
		if hit[0]:
			o.set_color((SLIDERS[0].value, SLIDERS[1].value, SLIDERS[2].value))
			return

def draw_mixer(d, x = MIXER_X, y = MIXER_Y, w = MIXER_WIDTH, h = MIXER_HEIGHT):
	global SLIDERS
	
	red = SLIDERS[0].value
	green = SLIDERS[1].value
	blue = SLIDERS[2].value
	
	w3rd, h3rd = w / 3, h / 3
	
	pygame.draw.rect(d, (red, 0, 0), (x, y, w3rd, h3rd), 0)
	pygame.draw.rect(d, (red, green, 0), (x + w3rd, y, w3rd, h3rd), 0)
	pygame.draw.rect(d, (0, green, 0), (x + w3rd * 2, y, w3rd, h3rd), 0)
	pygame.draw.rect(d, (red, 0, blue), (x, y + h3rd, w3rd, h3rd), 0)
	pygame.draw.rect(d, (red, green, blue), (x + w3rd, y + h3rd, w3rd, h3rd), 0)
	pygame.draw.rect(d, (0, green, blue), (x + w3rd * 2, y + h3rd, w3rd, h3rd), 0)
	pygame.draw.rect(d, (0, 0, blue), (x + w3rd, y + h3rd * 2, w3rd, h3rd), 0)
	
# MAIN LOOP ------------------------------------------------------------------------------------------------ MAIN LOOP
while True:
	event_handler()
	
	# draw the central circle
	pygame.draw.circle(DS, (SLIDERS[0].value, SLIDERS[1].value, SLIDERS[2].value), CENTER_POSITION_XY, CENTER_SIZE, 0)
	
	# draw slider bars and values
	for s in SLIDERS:
		s.draw(DS)
	
	draw_mixer(DS)
	
	# draw orbiting circles
	for o in ORBITALS:
		o.draw(DS)
	
	pygame.display.update()
	DS.fill([0,0,0])