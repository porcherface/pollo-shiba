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
		print("hello "+playername)

		Level(1)