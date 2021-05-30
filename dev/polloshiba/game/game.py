######################################################################
# file: game.py
# version: 1.0.0
# author: porcherface
# descr: handles a game session, acts as manager for scenes and levels
######################################################################

from .level import Level

class NewGame:
	def __init__(self, playername, lives, gamemode):
		if gamemode != "competition":
			raise NotImplementedError

		# handshake with player
		print("***********************")
		print("hello " + playername)
		print("***********************")
		
		print("launching level 1")	
		Level(1, playername)