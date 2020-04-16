#!/usr/bin/python
#
#	Battler.py
#		Parent class of Bug & Bself
#

import Dfile, pygame, functions
from pygame.locals import *
from functions import load_image

class Battler():
	def draw(self):
		ts=pygame.display.get_surface()
		tempx=self.off[0]+self.x*34
		tempy=self.off[1]+self.y*20
		ts.blit(self.sprite, (tempx, tempy))
	
	def setDir(self,dr):
		if dr==0:
			self.direction=0
			self.sprite=load_image("chars/"+self.type+"/"+self.name+"/"+Dfile.getAtr(self.dfile,"B","SPR"))
		if dr==90:
			self.direction=90
			self.sprite=load_image("chars/"+self.type+"/"+self.name+"/"+Dfile.getAtr(self.dfile,"B","SPU"))
		if dr==180:
			self.direction=180
			self.sprite=load_image("chars/"+self.type+"/"+self.name+"/"+Dfile.getAtr(self.dfile,"B","SPL"))
		if dr==270:
			self.direction=270
			self.sprite=load_image("chars/"+self.type+"/"+self.name+"/"+Dfile.getAtr(self.dfile,"B","SPD"))
