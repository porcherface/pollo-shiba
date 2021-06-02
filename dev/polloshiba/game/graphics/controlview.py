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
from .agent import Station

class ControlView:
	def __init__(self, mode = 'competition', agent_list = ""):
		


		self.back = pygame.image.load(os.path.join(RES_PATH,'res','control.png')).convert_alpha()
		self.rect = self.back.get_rect().move(0, 700)
		self.myfont = pygame.font.SysFont('Comic Sans MS', 40)

		self.agents = agent_list.split(",")
		print("agents detected by control panel: ")
		print(agent_list)
		self.stationlist = []
		for agent in self.agents:
			self.stationlist.append(Station(agent))
			print("saved station" + agent)

	def draw(self, screen):

		pos_y = 90
		print("go")

		for station in self.stationlist:
			self.back.blit(station.image, (150, pos_y))
			pos_y += 90

		screen.blit(self.back, self.rect)
