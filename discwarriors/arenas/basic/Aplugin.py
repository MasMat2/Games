#
#	Default Arena
#		Main file for default Arena
#		DO NOT DELETE!
#

import pygame, os
from pygame import *

def load_image(name, colorkey=True):
	fullname = os.path.join('', name)
	try:
		image = pygame.image.load(fullname)
	except pygame.error, message:
		print "Cannot load image:", name
		raise SystemExit, message
	image = image.convert()
	if colorkey:
		colorkey = image.get_at((0,0))
		image.set_colorkey(colorkey, RLEACCEL)
	return image
	
def enemies(enemy):
	if enemy=="teron":
		return [["teron",2,0]]
	else:
		return [[enemy,2,0]]

def sprite():
	return "arenas/basic/bak.png"

def draw(self,screen):
	btempx=0
	btempy=80
	screen.blit(self.sprite, (btempx,btempy))
			
def width():
	return 9

def height():
	return 6
	
def grid():
	grid=[
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0],
	[0,0,0,0,0,0,0,0,0]]
	return grid
