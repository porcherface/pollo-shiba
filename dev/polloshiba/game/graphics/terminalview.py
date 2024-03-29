######################################################################
# file: terminalview.py
# version: 1.0.0
# author: porcherface
# descr: src for terminal graphics
######################################################################
import pathlib
import os

RES_PATH = pathlib.Path(__file__).parent.absolute()

import pygame
from .msgbox import MsgBox

class TerminalView:
	def __init__(self, playername, lives, agent_list, mode = 'competition'):
		
		self.back = pygame.image.load(os.path.join(RES_PATH,'res','term.png')).convert_alpha()
		self.rect = self.back.get_rect().move(1000, 0)
		self.box = MsgBox(playername)
		self.box.drawLives(self.back,lives)
		self.box.drawName(self.back)
		if agent_list != "":
			self.box.drawAgents(self.back, agent_list)

	def draw(self, screen):
		screen.blit(self.back, self.rect)


	def drawAgents(self, agent_list):		
		self.box.drawAgents(self.back, agent_list)
