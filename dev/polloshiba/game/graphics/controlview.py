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
	def __init__(self, mode = 'competition', agent_list = None):
		
		if agent_list == None:
			count = 1312

		self.back = pygame.image.load(os.path.join(RES_PATH,'res','control.png')).convert_alpha()
		self.rect = self.back.get_rect().move(0, 700)
		self.myfont = pygame.font.SysFont('Comic Sans MS', 40)
		self.lazors = self.myfont.render("LAZOR COUNT: "+str(count), True, (255, 25, 31))

	def draw(self, screen):
		self.back.blit(self.lazors, self.lazors.get_rect().move(100,100))
		screen.blit(self.back, self.rect)
