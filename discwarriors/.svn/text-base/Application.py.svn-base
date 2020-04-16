# Disc Warriors
#
#	Application.py
#		Basic Game class for variables & state change
#

import pygame, sys, pickle, functions
import Arena, Area, Battler, Bself, Bbug, GUI, Wself, Wbug, Application
from pygame import *
from functions import *

class DiscWarriors:
	def __init__(self,width=306,height=200,state="Title"):
		try:
			import psyco
			psyco.full()
		except:
			print "Psyco not installed. It will not run at full speed."
		
		pygame.init()
		print "PyGame Initialized"
		self.width=width
		self.height=height
		self.screen=pygame.display.set_mode((self.width,self.height))
		pygame.display.set_caption('Disc Warriors')
		pygame.display.set_icon(pygame.image.load("resc/icon.png"))
		print "Window Set"
		self.font=pygame.font.Font('resc/Vera.ttf',16)
		self.Test=GUI.Menu(("Play","Exit"),"Title",25)
		self.backSpr=load_image("arenas/default/grid.png", False)
		self.state=state
		self.quit=False
		self.timer=pygame.time.Clock()
		self.fps=0
		print "Application Variables Set"
		self.arena=None
		self.area=None
	
	def getQuit(self, events):
		for event in events:
			if event.type == QUIT: 
				self.quit=True
				pygame.quit()
				sys.exit()
			if event.type==KEYDOWN:
				if event.key==K_ESCAPE:
					self.quit=True
					pygame.quit()
					sys.exit()
	
	def Main(self):
		if self.quit==False:
			Handler=pygame.event.get()
			self.screen.fill((0,0,0))
			if self.state=="World":
				if self.area==None:
					self.area=self.area=Area.Area(Wself.player("default.dfile"),"teron")
				temp=self.area.step(Handler)
				if temp!=None:
					if temp[0]=="Fight":
						self.arena=Arena.Arena(Bself.player("default.dfile"),temp[1])
						self.state="Fight"
			if self.state=="Title":
				temp=self.Test.step(self.screen,Handler,[])
				if temp!=None:
					self.state=temp
			if self.state=="Fight":
				#if pygame.mixer.music.get_busy()==False:
				#	pygame.mixer.music.load('resc/Brainkrieg.ogg')
				#	pygame.mixer.music.play()
				temp=self.arena.step(self.screen,Handler)
				if temp!=None:
					t2=[]
					for ID in temp:
						for c in range(0,len(self.area.grid)):
							if self.area.grid[c][0].group=="Bug" and self.area.grid[c][0].id==ID:
								t2.append(c)
					t2.sort(reverse=True)
					for num in t2:
						self.area.grid.pop(num)
					del t2
					self.state="World"
					#pygame.mixer.music.stop()
			
			self.fps=self.getFPS()
			self.screen.blit(self.font.render(self.fps,0,(255,0,0)), (0,0))
			self.timer.tick(30)
			
			pygame.display.flip()
			self.getQuit(Handler)
		else:
			exit()
	def getFPS(self):
		return str(1000/self.timer.get_time())
