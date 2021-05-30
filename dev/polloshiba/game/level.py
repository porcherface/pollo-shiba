######################################################################
# file: level.py
# version: 1.0.0
# author: porcherface
# descr: a level scene
######################################################################

from .interface import Interface
from .graphics.screen import GameScreen

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
	def __init__(self, num):

		# preparation 
		# setup lasers
		print("Initializing agents...")
		if num == 1:
			agent_list = InitAgents_L1()
		print("  [ OK ]  ")

		# draw graphics	
		print("Drawing graphics... ")

		# setting state


	def execute(self):
		pass





