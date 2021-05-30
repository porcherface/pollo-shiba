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

class TerminalView:
	def __init__(self, mode = 'competition'):
		
		self.back = pygame.image.load(os.path.join(RES_PATH,'res','term.png')).convert_alpha()
		self.rect = self.back.get_rect().move(1000, 0)
		
	def draw(self, screen):
		screen.blit(self.back, self.rect)