#!/usr/bin/python

import pygame, sys, os, math, string, random
from random import randint, seed
from pygame.locals import *

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

def dirx(length, direction):
	return length*math.cos(radian(direction))

def diry(length, direction):
	return length*math.sin(math.radians(direction))
	
def intrnd(num):
	return int(round(num))

def dist(obj1,obj2):
	i=math.sqrt(pow((obj1.x-obj2.x),2)+pow((obj1.y-obj2.y),2))
	return i

def getCord(x,y,dir):
	if dir==0:
		return [x+1,y]
	if dir==90:
		return [x,y-1]
	if dir==180:
		return [x-1,y]
	if dir==270:
		return [x,y+1]

chars=string.ascii_letters + string.digits
def bugID():
	seed()
	return chars[randint(0, 61)] + chars[randint(0, 61)] + chars[randint(0, 61)] + chars[randint(0, 61)] + chars[randint(0, 61)]
