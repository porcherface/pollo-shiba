######################################################################
# file: screen.py
# version: 1.0.0
# author: porcherface
# descr: graphics handler, blits, renders and update graphics for levels
######################################################################

import pygame
import pathlib

from .roomview import RoomView
from .terminalview import TerminalView
from .controlview import ControlView

RES_PATH = pathlib.Path(__file__).parent.absolute()

class GameScreen:
	def __init__(self):
		
		# risoluzione monitor 1
		RES_X = 1380
		RES_Y = 1080

		self.screen = pygame.display.set_mode([RES_X, RES_Y])

		# set background masks     
		room = RoomView()
		term = TerminalView()
		ctrl = ControlView()

		rect_1 = back_1.get_rect().move(0, 0)
		rect_2 = back_2.get_rect().move(1000, 0)
		rect_3 = back_3.get_rect().move(0, 700)
		rect_4 = back_4.get_rect().move(1000, 700)

		room = pygame.image.load(os.path.join(RES_PATH,'res','room.png')).convert_alpha()
		room_rect = room.get_rect().move(50,150)
		logo = pygame.image.load(os.path.join(RES_PATH,'res','minilogo.png')).convert_alpha()
		logo_rect = logo.get_rect().move(100,100)


	def draw(self):
		room.draw(self.screen)
		term.draw(self.screen)
		ctrl.draw(self.screen)

	def draw_fast(self)
		

