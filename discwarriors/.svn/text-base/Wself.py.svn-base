#Disc Warriors
#
#	Wself.py
#		Class for the character in the world
#

import Dfile, pygame, functions, GUI, math
from pygame.locals import *
from functions import load_image

class player(pygame.sprite.Sprite):
	def __init__(self,path):
		pygame.sprite.Sprite.__init__(self)
		self.dfile="dfiles/"+path
		self.name=Dfile.getName(self.dfile)
		self.type=Dfile.getType(self.dfile)
		self.group="Player"
		self.moving='N'
		self.off=(-16,-33)
		self.x=40
		self.y=40
		self.sprite=load_image("resc/player.png")
		self.action=False
		
		self.inc=5
		
	def update(self,events,sur,of1):
		keys=pygame.key.get_pressed()
		
		if keys[K_LEFT]:	
			if self.x>self.sprite.get_width()+self.off[0]:
				self.x-=self.inc
				
		if keys[K_RIGHT]:
			if self.x<sur.get_width()+self.off[0]:
				self.x+=self.inc
				
		if keys[K_UP]:
			if self.y>self.sprite.get_height()+self.off[1]:
				self.y-=self.inc
				
		if keys[K_DOWN]:
			if self.y<sur.get_height():
				self.y+=self.inc
				
		if self.x>sur.get_width()+self.off[0]:
			self.x=sur.get_width()+self.off[0]
			
		if self.x<self.sprite.get_width()+self.off[0]:
			self.x=self.sprite.get_width()+self.off[0]
			
		if self.y>sur.get_height():
			self.y=sur.get_height()
			
		if self.y<self.sprite.get_width():
			self.y=self.sprite.get_width()
			
		self.draw(sur,of1)

		return self.y
		
	def draw(self,surf,of2):
		pygame.draw.circle(surf,(0,0,0),(self.x-of2[0],self.y-of2[1]),2)
		tempx=self.x+self.off[0]-of2[0]
		tempy=self.y+self.off[1]-of2[1]
		surf.blit(self.sprite, (tempx,tempy))

	def num(self,x,y):
		if functions.dist(self,x)>functions.dist(self,y):
			return 1
		elif functions.dist(self,x)==functions.dist(self,y):
			return 0
		else:
			return -1
	
	def gsort(self,x):
		nGrid=[]
		x.sort(self.num)
		for item in x:
			nGrid.append([item,functions.dist(self,item)])
		del x
		return nGrid
