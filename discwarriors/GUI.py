#Disc Warriors
#
#	Button.py
#		Button class for the Title Screen
#

import pygame
from pygame import *

def longest(string):
	templ=0
	for x in range(0,len(string)):
		if len(string[x])>templ:
			templ=len(string[x])
	return templ

#This function returns a list of bugs in order of how
#close they are to the player. The first index is the
#object, the second is its distance.
def setGrid(grid):
	temp=[]
	for i in xrange(len(grid)):
		if grid[i][0].group=="Player":
			player=grid[i][0]
		else:
			temp.append(grid[i][0])
	grid=temp
	del temp
	return player.gsort(grid)

class Menu():
	def __init__(self,string,_type,size):
		self.font=pygame.font.Font('resc/Vera.ttf',size)
		self.selected=0
		self.string=string
		self.type=_type
		self.child=0
	
	def step(self,screen,events,grid):
		if self.type=="Title":
			tempos=len(self.string)
			screen.blit(self.font.render("Disc Warriors",0,(0,0,255)), (70,40))
			for pos in range(0,len(self.string)):
				if pos==self.selected:
					text=self.font.render(self.string[pos],0,(0,255,0))
					tempy=pos*30+90
					screen.blit(text, (120,tempy))
				elif pos!=self.selected:
					text=self.font.render(self.string[pos],0,(255,0,0))
					tempy=pos*30+90
					screen.blit(text, (120,tempy))
			for event in events:
				if event.type==KEYDOWN:
					if event.key==K_DOWN:
						if self.selected<len(self.string)-1:
							self.selected=self.selected+1
					if event.key==K_UP:
						if self.selected>0:
							self.selected=self.selected-1
					if event.key==K_RETURN:
						if self.selected==0:
							return "World"
						if self.selected==1:
							exit()
		if self.type=="Actions":
			if self.child==0:
				pygame.draw.rect(screen,(255,0,0),(20,20,45,60))	
				tempos=len(self.string)
				for pos in range(0,len(self.string)):
					if pos==self.selected:
						text=self.font.render(self.string[pos],0,(0,255,0))
						tempy=pos*11+20
						screen.blit(text, (22,tempy))
					elif pos!=self.selected:
						text=self.font.render(self.string[pos],0,(0,0,255))
						tempy=pos*11+20
						screen.blit(text, (22,tempy))
				for event in events:
					if event.type==KEYDOWN:
						if event.key==K_DOWN:
							if self.selected<len(self.string)-1:
								self.selected=self.selected+1
						if event.key==K_UP:
							if self.selected>0:
								self.selected=self.selected-1
						if event.key==K_RETURN:
							if self.selected==0:
								grid=setGrid(grid)
								if len(grid):
									if grid[0][1]<100:
										grid[0][0].selected=True
										self.add(0,("Ok","Info","Cancel"))
									else:
										print "No enemies in range"
								else:
									print "No enemies"
							if self.selected==1:
								return (True,0)
							if self.selected==2:
								self.child=0
								self.selected=0
								return (False,0)
					else:
						return (True,0)
			else:
				pygame.draw.rect(screen,(255,0,0),(20,20,45,60))
				for pos in range(0,len(self.string)):
					if pos==self.child["selected"]:
						text=self.font.render(self.string[pos],0,(0,255,0))
						tempy=pos*11+20
						screen.blit(text, (22,tempy))
					elif pos!=self.child["selected"]:
						text=self.font.render(self.string[pos],0,(0,0,255))
						tempy=pos*11+20
						screen.blit(text, (22,tempy))
				pygame.draw.rect(screen,(0,0,255),(30,30,45,60))
				for pos in range(0,len(self.child["str"])):
					if pos==self.selected:
						text=self.font.render(self.child["str"][pos],0,(0,255,0))
						tempy=pos*11+30
						screen.blit(text, (32,tempy))
					elif pos!=self.selected:
						text=self.font.render(self.child["str"][pos],0,(255,0,0))
						tempy=pos*11+30
						screen.blit(text, (32,tempy))
				for event in events:
					if event.type==KEYDOWN:
						if event.key==K_DOWN:
							if self.selected<len(self.child["str"])-1:
								self.selected=self.selected+1
						if event.key==K_UP:
							if self.selected>0:
								self.selected=self.selected-1
						#To go to the previous menu, set self.child and self.selected to 0
						#To exit out of the menu, do the same, but return False
						if event.key==K_RETURN:
							if self.selected==0:
								for item in grid:
									if item[0].group=="Bug":
										if item[0].selected:
											self.child=0
											self.selected=0
											return ("Fight",item[0])
							if self.selected==1:
								for item in grid:
									if item[0].group=="Bug":
										if item[0].selected:
											print item[0].health
							if self.selected==2:
								for item in grid:
									if item[0].group=="Bug":
										if item[0].selected:
											item[0].selected=False
								self.child=0
								self.selected=0
				
					
	def add(self,sel,string):
		self.child={"selected":sel,"str":string}
