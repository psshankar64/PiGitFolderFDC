'''
This script loads an image, creates ball objects and then bounces them around the display surface
'''
import sys
import random
import math

import pygame
import pygame.gfxdraw
from pygame.locals import *

pygame.init()

''' DISPLAY SETUP -------------------------------------------------------------------------------- DISPLAY SETUP '''
DISPLAY_WIDTH = 1240
DISPLAY_HEIGHT = 720
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

''' LOAD IMAGES ---------------------------------------------------------------------------------- LOAD IMAGES '''
# Load the image from a file
# Supported formats are JPEG, PNG, GIF
BALL = pygame.image.load('colorwheel_100.png')

# Get the dimensions of the image by calling the Surface get_rect() function
R = BALL.get_rect()

''' DATA TABLES ---------------------------------------------------------------------------------- DATA TABLE '''
# this list defines the direction vector for the ball to travel in. There are 360 possible directions
D2R = (math.pi * 2) / 360 # this converts radians to degrees
DIRECTION_VECTOR_LOOKUP = list([[math.cos(D2R * degrees), math.sin(D2R * degrees)] for degrees in xrange(360)])


''' FUNCTIONS AND CLASSES ------------------------------------------------------------------------ FUNCTIONS AND CLASSES '''
# define the ball class
class ball:
	x = 0.0
	y = 0.0
	def __init__(self, r = R):
		# because the script generations random positions for x, y it needs to know the x and y limits of those boundries
		global DISPLAY_WIDTH, DISPLAY_HEIGHT, DIRECTION_VECTOR_LOOKUP
		
		self.r = r # grab the image.get_rect() dimensions for use when drawing the image
		
		# randomly assign the x and y position to somewhere in the display surface
		self.x += random.randint(r.center[0], DISPLAY_WIDTH - r.center[0])
		self.y += random.randint(r.center[1], DISPLAY_HEIGHT - r.center[1])

		# define the direction vector based on 360 degrees
		self.dx, self.dy = DIRECTION_VECTOR_LOOKUP[random.randint(0, 359)]

	def draw(self, ds = DS, image = BALL):
		# this function draws the ball image centralised at its x, y coordinates
		# remember .center[0] = image.width / 2 and .center[1] = image.height / 2
		ds.blit(image, (self.x - self.r.center[0], self.y - self.r.center[1]))

	def move(self):
		global DISPLAY_WIDTH, DISPLAY_HEIGHT
		# this function moves the ball by adding the direction vector to the x and y coords then checks to see
		# if the ball has hit the sides of the display surface. if it has then change the direction of the ball
		
		# add the direction vector to the x, y coordinates
		self.x += self.dx
		self.y += self.dy
		
		# check if either the left or right side of the display surface has been 'hit'
		# and if true then switch the horizontal direction of the ball
		if self.x <= self.r.center[0] or self.x >= DISPLAY_WIDTH - self.r.center[0]:
			self.dx = -self.dx

		# check if either the top or bottom of the display surface has been 'hit'
		# and if true then switch the vertical direction of the ball
		if self.y <= self.r.center[1] or self.y >= DISPLAY_HEIGHT - self.r.center[1]:
			self.dy = -self.dy
	
	def do(self):
		self.move()
		self.draw()
		
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

			
			
''' DEFINE BALLS --------------------------------------------------------------------------------- DEFINE BALLS '''
# define the number of balls
nBALLS = 20

#create a list of balls
BALLS = list([ball() for count in xrange(nBALLS)])

''' MAIN LOOP ------------------------------------------------------------------------------------ MAIN LOOP '''
while True:
	event_handler()

	# iterate through the balls drawing and moving each in turn
	for b in BALLS:
		b.do()
		
	pygame.display.update()
	
	# it's important in the this script to clear the display surface after updating
	# overwise you'll see a trail of images as it moves from one side of the display
	# surface to the other. Try deleting the line below and running the script again!
	DS.fill([0,0,0])	
	
	
	
	
	
	
	
	
	
	
