#
#	Teron Plugin
#		Main file for the Teron bug
#

import random, sys
#sys.path.append("../../../")
import Battack

def update(self,grid):
	_grid=move(self,grid)
	self.draw()
	return _grid

def getCord(x,y,dir):
	if dir==0:
		return [x+1,y]
	if dir==90:
		return [x,y-1]
	if dir==180:
		return [x-1,y]
	if dir==270:
		return [x,y+1]

def move(self,grid):
	enemy=self.findPlayer(grid)
	if enemy==None:
		print "Player not found"
		raise SystemExit
	tmem=self.memory
	difx=abs(enemy.x-self.x)
	dify=abs(enemy.y-self.y)
	if tmem==0:
		self.memory=16
	if tmem==15:
		if enemy.x==self.x or enemy.y==self.y:
			grid[self.y][self.x]=0
			update=1
			if enemy.x>self.x and self.direction!=0:
				self.setDir(0)
			elif enemy.x>self.x and self.direction==0:
				grid=attack(self,grid)
			elif enemy.x<self.x and self.direction!=180:
				self.setDir(180)
			elif enemy.x<self.x and self.direction==180:
				grid=attack(self,grid)
			elif enemy.y>self.y and self.direction!=270:
				self.setDir(270)
			elif enemy.y>self.y and self.direction==270:
				grid=attack(self,grid)
			elif enemy.y<self.y and self.direction!=90:
				self.setDir(90)
			elif enemy.y<self.y and self.direction==90:
				grid=attack(self,grid)
			grid[self.y][self.x]=self
		if self.x>enemy.x and self.y!=enemy.y:
			if dify>difx:
				if grid[self.y][self.x-1]==0:
					grid[self.y][self.x]=0
					self.x=self.x-1
					self.setDir(180)
					self.memory=tmem-1
					grid[self.y][self.x]=self
		if self.x<enemy.x and self.y!=enemy.y:
			if dify>difx:
				if grid[self.y][self.x+1]==0:
					grid[self.y][self.x]=0
					self.x=self.x+1
					self.setDir(0)
					self.memory=tmem-1
					grid[self.y][self.x]=self
		if self.y>enemy.y and self.x!=enemy.x:
			if difx>dify:
				if grid[self.y-1][self.x]==0:
					grid[self.y][self.x]=0
					self.y=self.y-1
					self.setDir(90)
					self.memory=tmem-1
					grid[self.y][self.x]=self
		if self.y<enemy.y and self.x!=enemy.x:
			if difx>dify:
				if grid[self.y+1][self.x]==0:
					grid[self.y][self.x]=0
					self.y=self.y+1
					self.setDir(270)
					self.memory=tmem-1
					grid[self.y][self.x]=self
		if difx==dify:
			chance=random.randint(0,2)
			if chance==0:
				if self.x>enemy.x:
					if grid[self.y][self.x-1]==0:
						grid[self.y][self.x]=0
						self.x=self.x-1
						self.setDir(180)
						self.memory=self.memory-1
						grid[self.y][self.x]=self
				elif self.x<enemy.x:
					if grid[self.y][self.x+1]==0:
						grid[self.y][self.x]=0
						self.x=self.x+1
						self.setDir(0)
						self.memory=self.memory-1
						grid[self.y][self.x]=self
			elif chance==1:
				if self.y>enemy.y:
					if grid[self.y-1][self.x]==0:
						grid[self.y][self.x]=0
						self.y=self.y-1
						self.setDir(90)
						self.memory=self.memory-1
						grid[self.y][self.x]=self
				elif self.y<enemy.y:
					if grid[self.y+1][self.x]==0:
						grid[self.y][self.x]=0
						self.y=self.y+1
						self.setDir(270)
						self.memory=self.memory-1
						grid[self.y][self.x]=self
	else:
		self.memory=self.memory-1
	return grid

def attack(bug,_grid):
	i=getCord(bug.x,bug.y,bug.direction)
	if _grid[i[1]][i[0]]!=0:
		if _grid[i[1]][i[0]].group=="Player":
			_grid[i[1]][i[0]].health-=30
			if _grid[i[1]][i[0]].health<0:
				_grid[i[1]][i[0]].health=0
	else:
		_grid[i[1]][i[0]]=Battack.attack(bug,"default")
	del i
	return _grid
