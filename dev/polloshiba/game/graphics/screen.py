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


class GameScreen:
	def __init__(self):
		
		# risoluzione monitor 1
		RES_X = 1380
		RES_Y = 1080

		self.screen = pygame.display.set_mode([RES_X, RES_Y])

		# set background masks     
		self.room = RoomView()
		self.term = TerminalView()
		self.ctrl = ControlView()
		self.doge = DogeView()
		
	''' this is an idle time draw, it is performed before execution'''
	def draw(self):
		self.room.draw(self.screen)	
		self.term.draw(self.screen)
		self.ctrl.draw(self.screen)
		self.doge.draw(self.screen)

		pygame.display.flip()
		pygame.display.update()

	''' this is a execution time draw, it is important to keep it minimal ''' 
	def draw_fast(self):
		pass

