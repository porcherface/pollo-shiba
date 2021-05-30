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

class RoomView:
	def __init__(self, mode = 'competition'):
		
		self.back = pygame.image.load(os.path.join(RES_PATH,'res','map.png')).convert_alpha()
		self.rect = self.back.get_rect()

		self.map = pygame.image.load(os.path.join(RES_PATH,'res','room.png')).convert_alpha()
		self.mrect = self.map.get_rect().move(100,100)
		
		self.states = []
		self.states.append(pygame.image.load(os.path.join(RES_PATH,'res','s0.png')).convert_alpha())
		self.states.append(pygame.image.load(os.path.join(RES_PATH,'res','s1.png')).convert_alpha())

		self.states.append(pygame.image.load(os.path.join(RES_PATH,'res','s0.png')).convert_alpha())
		self.states.append(pygame.image.load(os.path.join(RES_PATH,'res','s0.png')).convert_alpha())
		
		self.srect = self.states[0].get_rect().move(100,440)

		self.img = self.back

		self.drawMap()
		self.drawState(0)

	def draw(self, screen):
		screen.blit(self.img, self.rect)

	def drawState(self, state):
		self.img = self.back
		self.img.blit(self.states[state], self.srect)

	def drawMap(self):	
		self.back.blit(self.map, self.mrect)


