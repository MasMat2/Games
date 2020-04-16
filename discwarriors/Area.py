#Disc Warriors
#
#	Area.py
#		World class for E-World areas
#

import pygame, Wself, Wbug, GUI, sys, functions
from pygame.locals import *

def num(x,y):
	if x[1]>y[1]:
		return 1
	elif x[1]==y[1]:
		return 0
	else:
		return -1

class Area():
	def __init__(self, player, enemy):
		self.Menu=GUI.Menu(("Engage","Talk","Exit"),"Actions",10)
		ARplugin=None
		sys.path.append("area/default")
		import ARplugin
		self.draw=ARplugin.draw
		self.width=ARplugin.width()
		self.height=ARplugin.height()
		self.grid=[]
		self.off=[0,0]
		self.sprite=functions.load_image(ARplugin.sprite(),False)
		self.temp=pygame.Surface((self.width,self.height)) 
		self.action=False
		
		ids=[] 
		for nme in ARplugin.enemies(enemy):
			bid=functions.bugID()
			while bid in ids:
				bid=functions.bugID()
			string=nme[0]+".dfile"
			bug=Wbug.bug(string,bid)
			bug.x=nme[1]
			bug.y=nme[2]
			self.grid.append([bug,bug.y])
		del ids
			
		self.grid.append([player,player.y])
		
		sys.path.pop()
		
	def step(self,events):
		self.temp.blit(self.sprite,(-self.off[0],-self.off[1],self.width,self.height))
		screen=pygame.display.get_surface()
		for event in events:
			if event.type==KEYDOWN:
				if event.key==K_RETURN:
					if self.action==False:
						self.action=True
						events=-1
						break
		if self.action==False:
			self.grid.sort(num)
		
		for i in range(0,len(self.grid)):
			if self.action==False:
				self.grid[i][1]=self.grid[i][0].update(events,self.temp,self.off)
				if self.grid[i][0].group=="Player":
					if self.grid[i][0].x>(screen.get_width()/2):
						self.off[0]=self.grid[i][0].x-(screen.get_width()/2)
					if self.grid[i][0].y>(screen.get_height()/2):
						self.off[1]=self.grid[i][0].y-(screen.get_height()/2)
					if self.off[0]<0:
						self.off[0]=0
					if self.off[1]<0:
						self.off[1]=0
					if self.off[0]>self.sprite.get_width()-screen.get_width():
						self.off[0]=self.sprite.get_width()-screen.get_width()
					if self.off[1]>self.sprite.get_height()-screen.get_height():
						self.off[1]=self.sprite.get_height()-screen.get_height()
			else:
				self.grid[i][0].draw(self.temp,self.off)
		if self.grid==[]:
			print "ERROR OCCURRED IN GRID!"
			exit()
		self.draw(self,screen)
		pygame.draw.circle(screen,(255,255,255),(screen.get_width()/2,screen.get_height()/2),2)
		
		if self.action==True:
			if events!=-1:
				temp=self.Menu.step(pygame.display.get_surface(),events,self.grid)
				if temp==None:
					temp=(True,0)
			else:
				temp=(True,0)
			if temp[0]==False:
				self.action=False
			elif temp[0]==True:
				return None
			elif temp[0]=="Fight":
				self.action=False
				return temp
