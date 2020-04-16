#!/usr/bin/python
#
#	Bbug.py
#		Bug class for battling
#

import Dfile, pygame, functions, Battler, sys
from pygame.locals import *
from functions import load_image

class Bug(Battler.Battler,pygame.sprite.Sprite):
	def __init__(self,path,_x,_y,ID):
		pygame.sprite.Sprite.__init__(self)
		Bplugin=None
		pygame.sprite.Sprite.__init__(self)
		self.dfile="dfiles/"+path
		self.name=Dfile.getName(self.dfile)
		self.type=Dfile.getType(self.dfile)
		self.group="Bug"
		sys.path.append("./chars/"+self.type+"/"+self.name)
		import Bplugin
		self.update=Bplugin.update
		self.direction=270
		self.off=(int(Dfile.getAtr(self.dfile,"B","offx")),int(Dfile.getAtr(self.dfile,"B","offy")))
		self.id=ID
		self.x=_x
		self.y=_y
		self.sprite=load_image("chars/"+self.type+"/"+self.name+"/"+Dfile.getAtr(self.dfile,"B","SPD"))
		self.memory=15
		self.health=100
		sys.path.pop()
	
	def findPlayer(self,grid):
		for yTemp in range(0,len(grid)):
			for x in range(0,len(grid[0])):
				y=y=len(grid)-1-yTemp
				if grid[y][x]!=0 and grid[y][x]>0:
					if grid[y][x].group=="Player":
						return grid[y][x]
					else:
						continue