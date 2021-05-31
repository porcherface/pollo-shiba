######################################################################
# file: leaderboard.py
# version: 1.0.0
# author: porcherface
# descr: src for leaderboard graphics
######################################################################

class LeaderBoard:
	def __init__(self):
		# risoluzione monitor 1
		RES_X = 1380
		RES_Y = 1080

		self.screen = pygame.display.set_mode([RES_X, RES_Y])#pygame.FULLSCREEN

	def draw(self):