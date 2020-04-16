#!/usr/bin/python
#
#	Default Arena
#		Main file for default Arena
#		DO NOT DELETE!
#

import pygame, sys, os
from pygame import *
	
def enemies(enemy):
	if enemy=="teron":
		return [["teron",95,70],["teron",217,140]]
	else:
		if len(enemy)>1:
			ret=[]
			for x in range(0,len(enemy)):
				ret.append([enemy[x],x*20,x*20])
		else:
			return [[enemy,95,20]]

def sprite():
	return "area/default/bg.png"

def draw(self,screen):
	screen.blit(self.temp, (0,0,self.width,self.height))
			
def width():
	return 712

def height():
	return 600
