######################################################################
# file: level.py
# version: 1.0.0
# author: porcherface
# descr: a level scene
######################################################################

import pygame

from .interface import Interface
from .graphics.screen import GameScreen

FPS = 40
clock = pygame.time.Clock()

stationif = Interface()

''' 
this function contains hardcoded messages for level 1 structure
returns an agent class for each initialized agent. if at least 1
of the agents is not correctly intialized this function returns None
'''
def InitAgents_L1():

	# hardcoded messages for level1
	print("sending init message to stations...")
	MSG_1 = "#init$S01$E01E02@"
	MSG_2 = "#init$S02$E04@"
	MSG_3 = "#init$S03$R01R02@"
	MSG_4 = "#init$S04$R04@"

	print("expecting 4 acks...")

	# send init message to stations
	stationif.send(MSG_1, 1)
	stationif.waitack(1)

	stationif.send(MSG_2, 2)
	stationif.waitack(2)
	
	stationif.send(MSG_3, 3)
	stationif.waitack(3)
	
	stationif.send(MSG_4, 4)
	stationif.waitack(4)


class Level:
	def __init__(self, num, playername):

		# preparation 
		# setup lasers
		print("Initializing agents...")
		if num == 1:
			print("[SKIPPED]")
			# agent_list = InitAgents_L1()
		print("  [ OK ]  ")


		# draw graphics	
		self.screen = GameScreen(playername)
		
		# setting state
		print("setting room state...")

		print("setting up timer")
		if num == 1:
			timer = 200



		print("Drawing graphics... ")
		
		self.screen.setState(0)
		self.screen.draw()

		print("entering into exec loop...")
		self.execute()

	def execute(self):

		# events to register:
		# start button, 
		# intermediate button
		# dead!
		# timeout
		# win

		running = True
		while running:
			events = pygame.event.get()
			for event in events:
				self.handle_events(event)

			clock.tick(FPS)	


	def handle_events(self, event): 
		
		if event.type == pygame.KEYDOWN:
			if event.key == ord('a'):
				self.screen.setState(1)    
				self.screen.draw()





