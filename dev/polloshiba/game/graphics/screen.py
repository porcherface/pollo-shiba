######################################################################
# file: screen.py
# version: 1.0.0
# author: porcherface
# descr: graphics handler, blits, renders and update graphics for levels
######################################################################

import pygame
import pathlib
import os 

from .roomview import RoomView
from .terminalview import TerminalView
from .controlview import ControlView
from .dogeview import DogeView
from .timer import Timer

class GameScreen:
	def __init__(self, playername, level, lives, agent_list=None):
		
		# risoluzione monitor 1
		RES_X = 1380
		RES_Y = 1080

		self.screen = pygame.display.set_mode([RES_X, RES_Y])#pygame.FULLSCREEN
		# set background masks   
		self.room = RoomView(level)
		self.term = TerminalView(playername,lives)
		self.ctrl = ControlView('competition',agent_list)
		self.doge = DogeView()

		print("setting up timer -")
		if level == 1:
			start_time = 300
		if level == 2:
			start_time = 120
		if level == 3:
			start_time = 60
		print("timer is "+str(start_time)+" seconds.")
		self.timer = Timer(start_time)
		self.timer.position(700,530)

		self.state = 0
		
	''' this is an idle time draw, it is performed before execution'''
	def draw(self):

		self.room.draw(self.screen)	
		self.term.draw(self.screen)
		self.ctrl.draw(self.screen)
		self.doge.draw(self.screen)
		self.timer.draw(self.screen)

		pygame.display.flip()
		pygame.display.update()

	def setState(self,state):
		self.state = state
		self.room.drawState(state)
		self.room.draw(self.screen)

	''' this is a execution time draw, it is important to keep it minimal ''' 
	def draw_fast(self):
		self.room.draw(self.screen)	
		self.timer.draw(self.screen)
		pygame.display.flip()
		pygame.display.update()

