#!/usr/bin/python
#
#	Battack.py
#		Attack class for battlers
#

import functions, pygame, sys
from pygame import *
from functions import getCord

class attack(pygame.sprite.Sprite):
	def __init__(self, parent, name):
		pygame.sprite.Sprite.__init__(self)
		Atkplugin=None
		sys.path.append("./atk/"+name)
		import Atkplugin
		self.damage=Atkplugin.damage()
		self.off=Atkplugin.off()
		self.direction=Atkplugin.direction(parent)
		self.cord=Atkplugin.cord(self,parent)
		self.update=Atkplugin.update
		self.draw=Atkplugin.draw
		
		self.type=parent.type
		self.group="Attack"
		self.sprite=functions.load_image("atk/default/basic.png")
		self.attack=attack
		self.step=14
		Atkplugin=None
