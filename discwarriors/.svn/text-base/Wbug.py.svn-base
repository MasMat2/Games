#Disc Warriors
#
#	Wbug.py
#		Class for World based bugs.
#
#		This is, so far, not a useable
#		class. This is currently just a
#		test to get the basics of the
#		class to work.
#

import Dfile, pygame, functions
from pygame.locals import *
from functions import load_image

class bug(pygame.sprite.Sprite):
	def __init__(self,path,ID):
		pygame.sprite.Sprite.__init__(self)
		self.dfile="dfiles/"+path
		self.name=Dfile.getName(self.dfile)
		self.type=Dfile.getType(self.dfile)
		self.group="Bug"
		self.x=int(Dfile.getAtr(self.dfile,"W","Startx"))
		self.y=int(Dfile.getAtr(self.dfile,"W","Starty"))
		self.id=ID
		self.off=(-17,-32)
		self.sprite=load_image("chars/bugs/teron/teron_D.png")
		self.selected=False
		self.health=100
		
	def update(self,events,sur,of1):
		self.draw(sur,of1)
		return self.y
		
	def draw(self,surf,of2):
		tempx=self.x+self.off[0]-of2[0]
		tempy=self.y+self.off[1]-of2[1]
		surf.blit(self.sprite, (tempx,tempy))
		if self.selected:
			ox=self.x-of2[0]
			oy=self.y+self.off[1]-of2[1]
			pygame.draw.circle(surf,(0,0,0),(ox,oy),2)
		del tempx
		del tempy