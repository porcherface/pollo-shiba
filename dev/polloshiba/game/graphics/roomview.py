######################################################################
# file: roomview.py
# version: 1.0.0
# author: porcherface
# descr: src for roomview graphics
######################################################################
import pathlib
import os

RES_PATH = pathlib.Path(__file__).parent.absolute()

import pygame

from .timer import Timer

class RoomView:
	def __init__(self, level, mode = 'competition'):
		
		self.back = pygame.image.load(os.path.join(RES_PATH,'res','map.png')).convert_alpha()
		self.rect = self.back.get_rect()

		self.map = pygame.image.load(os.path.join(RES_PATH,'res','room'+str(level)+'.png')).convert_alpha()
		self.mrect = self.map.get_rect().move(100,100)
		
		self.states = []
		self.states.append(pygame.image.load(os.path.join(RES_PATH,'res','s0.png')).convert_alpha())
		self.states.append(pygame.image.load(os.path.join(RES_PATH,'res','s1.png')).convert_alpha())
		self.states.append(pygame.image.load(os.path.join(RES_PATH,'res','s2.png')).convert_alpha())
		self.states.append(pygame.image.load(os.path.join(RES_PATH,'res','s3.png')).convert_alpha())
		self.states.append(pygame.image.load(os.path.join(RES_PATH,'res','s4.png')).convert_alpha())
		self.srect = self.states[0].get_rect().move(50,440)

		self.img = self.back

		if level != 0:
			self.drawMap()
			self.drawState(0)

	def draw(self, screen):
		screen.blit(self.img, self.rect)

	def drawState(self, state):
		self.img.blit(self.back, self.rect)
		self.img.blit(self.states[state], self.srect)

	def drawMap(self):	
		self.back.blit(self.map, self.mrect)

	def drawTimer(self, screen):
		self.timer.draw(screen,pygame.time.get_ticks())
