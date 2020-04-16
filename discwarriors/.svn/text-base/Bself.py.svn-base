#!/usr/bin/env python
#
#	Bself.py
#		Player class for battling
#

import Dfile, pygame, functions, Battler, Battack
from pygame.locals import *
from functions import *

class player(Battler.Battler,pygame.sprite.Sprite):
	def __init__(self,path):
		pygame.sprite.Sprite.__init__(self)
		self.dfile="dfiles/"+path
		self.name=Dfile.getName(self.dfile)
		self.type=Dfile.getType(self.dfile)
		self.group="Player"
		self.direction=270
		self.off=(int(Dfile.getAtr(self.dfile,"B","offx")),int(Dfile.getAtr(self.dfile,"B","offy")))
		self.x=int(Dfile.getAtr(self.dfile,"B","Startx"))
		self.y=int(Dfile.getAtr(self.dfile,"B","Starty"))
		self.rect=pygame.Rect(self.x,self.y,0,0)
		self.health=100
		self.sprite=load_image("chars/"+self.type+"/"+self.name+"/"+Dfile.getAtr(self.dfile,"B","SPD"))
		self.motion=[0,0,0,0]

	def update(self,grid,events):
		if self.health<0:
			grid[self.y][self.x]=0
			return grid
		keys=pygame.key.get_pressed()
		if keys[K_LEFT]:
			if self.x>0:
				if grid[self.y][self.x-1]==0:
					grid[self.y][self.x]=0
					self.x=self.x-1
					self.setDir(180)
					grid[self.y][self.x]=self
		if keys[K_RIGHT]:
			if self.x<8:
				if grid[self.y][self.x+1]==0:
					grid[self.y][self.x]=0
					self.x=self.x+1
					self.setDir(0)
					grid[self.y][self.x]=self
		if keys[K_UP]:
			if self.y>0:
				if grid[self.y-1][self.x]==0:
					grid[self.y][self.x]=0
					self.y=self.y-1
					self.setDir(90)
					grid[self.y][self.x]=self
		if keys[K_DOWN]:
			if self.y<5:
				if grid[self.y+1][self.x]==0:
					grid[self.y][self.x]=0
					self.y=self.y+1
					self.setDir(270)
					grid[self.y][self.x]=self
		
		for event in events:
			if event.type==KEYDOWN:
				if event.key==K_SPACE:
					i=getCord(self.x,self.y,self.direction)
					if i[0]<9 and i[0]>-1 and i[1]>-1 and i[1]<6:
						if grid[i[1]][i[0]]!=0:
							if grid[i[1]][i[0]].group=="Bug":
								grid[i[1]][i[0]].health-=30
								if grid[i[1]][i[0]].health<0:
									grid[i[1]][i[0]].health=0
						else:
							grid[i[1]][i[0]]=Battack.attack(self,"default")
		self.draw()
		return grid
