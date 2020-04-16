#!/usr/bin/env python
#
#	DiscWarriors.py
#		Main Project File
#

import pygame, Application
from pygame.locals import *

if not pygame.font:
	print 'FONT MODULE IS NEEDED!'
	sys.exit(0)
if not pygame.mixer:
	print 'SOUND MODULE IS NEEDED!'
	sys.exit(0)

print "Disc Warriors started"

game=Application.DiscWarriors()

print "Application Created"

if __name__ == '__main__':
	print "Game Started"
	while 1:
		game.Main()
