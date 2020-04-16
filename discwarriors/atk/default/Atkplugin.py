#
#	Default Attack
#		Main file for default Attack
#		DO NOT DELETE!
#
#		self.x=self.off[0]+self.cord[0]*34
#		self.y=self.off[1]+self.cord[0]*20+80

import pygame

def sprite():
	return "atk/default/basic.png"

def damage():
	return 30

def off():
	return (9,83)

def getCord(x,y,dir):
	if dir==0:
		return [x+1,y]
	if dir==90:
		return [x,y-1]
	if dir==180:
		return [x-1,y]
	if dir==270:
		return [x,y+1]

def direction(parent):
	return parent.direction

def cord(self,parent):
	return getCord(parent.x,parent.y,self.direction)

def width():
	return 1

def height():
	return 1

def move(self,grid):
	tstep=self.step
	Pcord=self.cord
	if tstep==0:
		self.step=16
	if tstep==15:
		grid[self.cord[1]][self.cord[0]]=0
		self.cord=getCord(self.cord[0],self.cord[1],self.direction)
		#Check if it is out of the coordinates
		if self.cord[0]<0:
			grid[Pcord[1]][Pcord[0]]=0
			return grid
		elif self.cord[0]>8:
			grid[Pcord[1]][Pcord[0]]=0
			return grid
		elif self.cord[1]<0:
			grid[Pcord[1]][Pcord[0]]=0
			return grid
		elif self.cord[1]>5:
			grid[Pcord[1]][Pcord[0]]=0
			return grid
		if grid[self.cord[1]][self.cord[0]]!=0:
			if self.type!=grid[self.cord[1]][self.cord[0]].type:
				if self.damage>=grid[self.cord[1]][self.cord[0]].health:
					grid[self.cord[1]][self.cord[0]].health=0
					self.damage=0
					return grid
				else:
					grid[self.cord[1]][self.cord[0]].health-=self.damage
					self.damage=0
					return grid
		else:
			grid[self.cord[1]][self.cord[0]]=self
			self.draw(self)
		self.step-=1
	else:
		if self.cord[0]<0:
			grid[Pcord[1]][Pcord[0]]=0
			return grid
		elif self.cord[0]>8:
			grid[Pcord[1]][Pcord[0]]=0
			return grid
		elif self.cord[1]<0:
			grid[Pcord[1]][Pcord[0]]=0
			return grid
		elif self.cord[1]>5:
			grid[Pcord[1]][Pcord[0]]=0
			return grid
		self.step-=1
		draw(self)
	return grid

def draw(self):
	ts=pygame.display.get_surface()
	tempx=self.off[0]+self.cord[0]*34
	tempy=self.off[1]+self.cord[1]*20
	ts.blit(self.sprite, (tempx, tempy))

def update(self,grid):
	_grid=move(self,grid)
	return _grid
