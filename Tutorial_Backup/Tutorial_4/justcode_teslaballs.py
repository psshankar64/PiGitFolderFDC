'''
This script loads two images, creates a list of TESLA objects and bounces them off the bottom of the
display surface, rotating as they rise and fall.
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
DISPLAY_WIDTH = 1280
DISPLAY_HEIGHT = 720
DW_HALF = DISPLAY_WIDTH / 2
DH_HALF = DISPLAY_HEIGHT / 2
DISPLAY_AREA = DISPLAY_WIDTH * DISPLAY_HEIGHT
DS = pygame.display.set_mode((DISPLAY_WIDTH, DISPLAY_HEIGHT))

''' LOAD IMAGES ---------------------------------------------------------------------------------- LOAD IMAGES '''
# In the line below we create a container list for two frames of animation. TESLA[0] holds the first frame,
# TESLA[1] holds the second. An animation effect can be created by alternating between TESLA index 1 and 0. 
TESLA = list([
	pygame.image.load('teslaballs_1.png'),
	pygame.image.load('teslaballs_2.png')])
# because teslaballs_1.png and teslaballs_2.png have the same dimension we can just use one image to get the rect information
# such as width, height and center points
RECT = TESLA[0].get_rect()

''' SETUP VARIABLES ------------------------------------------------------------------------------ SETUP VARIABLES '''
# Because we don't won't the tesla object to jump out of the visible area of our display surface, a jump height
# restriction is necessary. If the tesla object drops below the MIN_JUMP_HEIGHT then the jumping height returns to
# MAX_JUMP_HEIGHT and starts again
MAX_JUMP_HEIGHT = DISPLAY_HEIGHT - RECT.center[1]
MIN_JUMP_HEIGHT = 50
	
''' DATA TABLES ---------------------------------------------------------------------------------- DATA TABLES '''
# The direction of the tesla object is either left (-1) or right (1). If the object hits the sides of the
# display surface then the variable tesla_ball.direction switches between 0 and 1 to index the DIRECTIONS list
# below. 0 = -1, 1 = 1
DIRECTIONS = list([-1, 1])

# The ball needs to bounce as though effected by gravity (although not accurately). I've always thought that math.cos
# and math.sin were relatively resource intensive functions I collate a list of cos/sin results before the main loop
# and just index those results when needed. Looking up a table is quick than working out cos and sin
D2R = (math.pi * 2) / 360 # this converts radians to degrees
BOUNCE = list([math.sin(D2R * degs) for degs in xrange(0, 180)])

''' FUNCTIONS AND CLASSES ------------------------------------------------------------------------ FUNCTIONS AND CLASSES '''
def rotate_and_center(ds, x, y, image, degrees):
	# This function rotates an image and draws it on the display surface centered at x, y
	rotated = pygame.transform.rotate(image, degrees)
	rect = rotated.get_rect()
	DS.blit(rotated, (x - rect.center[0], y - rect.center[1]))
	
class tesla_ball:
	# this object defines the tesla object
	x = 0.0 # predefine x as a floating point number
	
	def __init__(self):
		# this function initialises the tesla_ball object
		global DISPLAY_WIDTH
		global DIRECTIONS, MIN_JUMP_HEIGHT, MAX_JUMP_HEIGHT
		
		# no parameters are required to create a tesla_ball object because all the variables given random values
		self.x += random.randint(1, DISPLAY_WIDTH - 1) # set the horizontal starting position of the tesla object
		self.direction = DIRECTIONS[random.randint(0,1)] # 0 = -1, 1 = 1
		self.frame = random.randint(0, 1) # this is the TESLA list index for the animation
		self.height = random.randint(MIN_JUMP_HEIGHT, MAX_JUMP_HEIGHT) # starting height 
		self.height_progress = random.randint(0, 179) # this indexes the BOUNCE list in the data table section
		self.rotation = random.randint(0, 180) * 2 # starting rotation of the tesla object
		
	def move(self):
		# move() uses tesla_ball.direction, and tesla_ball.height_process to bounce the tesla object,
		# move it from side to side and rotates it.
		global MIN_JUMP_HEIGHT, MAX_JUMP_HEIGHT
		
		self.x += self.direction # add the direction to the horizontal position .direction can equal -1, 1
		
		# if the the horizontal position of the tesla object has 'hit' the edge of the display surface
		# then change direction -1 = 1, 1 = -1
		if self.x >= DISPLAY_WIDTH or self.x <= 0:
			self.direction = -self.direction
			
		# cycle through the .height_progess to simulate bouncing. value is limited to 0 - 179. When 179 is
		# reached the value is reset back to 0 and a new bounce starts
		if self.height_progress < 179:
			self.height_progress += 1
		else:
			self.height_progress = 0

			# also when the .height_progress reaches 179 the .height of the bounce is reduced by a random
			# number between 50 and 100 and if the .height value drops below the MIN_JUMP_HEIGHT it's reset
			# to the MAX_JUMP_HEIGHT
			self.height -= random.randint(50, 100)
			if self.height < MIN_JUMP_HEIGHT:
				self.height = MAX_JUMP_HEIGHT
				
		# increment the .rotation by 2 degrees. This is 2 degrees because the bounce takes exactly 180 moves
		# to complete and a full 360 degree rotation is desired during a single jump. 360 / 180 = 2
		# if the .rotation reaches 360 then reset back to 0
		self.rotation += 2
		if self.rotation == 360:
			self.rotation = 0
			
	def draw(self, ds = DS):
		# this function calls the rotate_and_center function. The position of the tesla object is calculated
		# as (.x, BOUNCE[.height_progress] * .height)
		global TESLA
		global DISPLAY_HEIGHT
		global BOUNCE
		
		rotate_and_center(ds, self.x, DISPLAY_HEIGHT - (BOUNCE[self.height_progress] * self.height), TESLA[self.frame], self.rotation)
		
		# alternate between displaying teslaballs_1.png and teslaballs_2.png by indexing the TESLA list with
		# either 0 or 1
		self.frame = 1 - self.frame
		
	def do(self):
		# This function merges .move(), .draw() functions into one
		self.move()
		self.draw()
		
def event_handler():
	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
			pygame.quit()
			sys.exit()

''' CONSTRUCTION --------------------------------------------------------------------------------- CONSTRUCTION '''
MAX_TESLA_BALLS = 20 # this sets the number of tesla objects to be created

# create a list of tesla_ball object with a count of MAX_TESLA_BALLS
TESLA_BALLS = list([tesla_ball() for count in xrange(MAX_TESLA_BALLS)])
			
''' MAIN LOOP ------------------------------------------------------------------------------------ MAIN LOOP '''
while True:
	event_handler()
	
	# iterate through the list of tesla_ball/s moving and drawing each one in turn
	for tb in TESLA_BALLS:
		tb.do()
	
	# update the primary display surface
	pygame.display.update()
	
	CLOCK.tick(30) # *** NOT COVERED IN THE VIDEO ***
	
	# clear the display surface to black
	DS.fill([0,0,0])