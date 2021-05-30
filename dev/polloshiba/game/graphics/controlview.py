######################################################################
# file: controlview.py
# version: 1.0.0
# author: porcherface
# descr: src for control view graphics
######################################################################

import pathlib
import os

RES_PATH = pathlib.Path(__file__).parent.absolute()

import pygame

class ControlView:
	def __init__(self, mode = 'competition'):
		
		self.back = pygame.image.load(os.path.join(RES_PATH,'res','control.png')).convert_alpha()
		self.rect = self.back.get_rect().move(0, 700)
		
	def draw(self, screen):
		screen.blit(self.back, self.rect)