#Disc Warriors
#
#	Arena.py
#		Arena class for battlers
#

import sys, functions, Bbug, Bself

class Arena():
	def __init__(self,player,enemy):
		Aplugin=None
		sys.path.append("arenas/basic")
		import Aplugin
		self.draw=Aplugin.draw
		self.width=Aplugin.width()
		self.height=Aplugin.height()
		self.grid=Aplugin.grid()
		self.sprite=functions.load_image(Aplugin.sprite(),False)
		self.EnmCount=0
		self.dead=[]
		sys.path.pop()
		
		for nme in Aplugin.enemies(enemy.name):
			string=nme[0]+".dfile"
			self.grid[nme[2]][nme[1]]=Bbug.Bug(string,nme[1],nme[2],enemy.id)
			self.EnmCount+=1
			
		self.grid[player.y][player.x]=player
		updated=[]
		
	def step(self,screen,events):
		alive=False
		self.draw(self,screen)
		updated=[]

		for y in xrange(0,len(self.grid)):
			for x in xrange(0,len(self.grid[0])):
				if self.grid[y][x]!=0 and self.grid[y][x]>0:
					if self.grid[y][x] not in updated:
						updated.append(self.grid[y][x])
						if self.grid[y][x].group=="Player":
							if self.grid[y][x].health!=0:
								self.grid=self.grid[y][x].update(self.grid,events)
								alive=True
							else:
								self.grid[y][x]=0
								alive=False
							if self.grid==None:
								print "Grid value is missing!"
								raise SystemExit
						elif self.grid[y][x].group=="Bug":
							if self.grid[y][x].health!=0:
								self.grid=self.grid[y][x].update(self.grid[y][x],self.grid)
							else:
								self.dead.append(self.grid[y][x].id)
								self.grid[y][x]=0
								self.EnmCount=0
							if self.grid==None:
								print "Grid value is missing!"
								raise SystemExit
						elif self.grid[y][x].group=="Attack":
							if self.grid[y][x].damage!=0:
								self.grid=self.grid[y][x].update(self.grid[y][x],self.grid)
							if self.grid==None:
								print "Grid value is missing!"
								raise SystemExit
		del updated
		if alive==False:
			print "You died."
			sys.exit(0)
		if self.EnmCount==0:
			return self.dead
		else:
			return None
