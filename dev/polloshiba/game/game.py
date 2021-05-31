######################################################################
# file: game.py
# version: 1.0.0
# author: porcherface
# descr: handles a game session, acts as manager for scenes and levels
######################################################################

from .level import Level
from .graphics.screen import GameScreen

class NewGame:
	def __init__(self, playername, lives, gamemode):
		if gamemode != "competition":
			raise NotImplementedError

		# handshake with player
		print("***********************")
		print("hello " + playername)
		print("you have "+str(lives)+" lives")
		print("***********************")
		

		print("initializing ui ")
		#screen = GameScreen(playername, 0, lives)
		
		level = 1	
		if type(lives) != type(5):
			print("something wrong with input, setting to 1")
		if lives < 0 or lives > 3:
			print("too many lives, baby, setting to 1")
			lives = 1
		
		last_good_time = "---.---"
		while level <= 3 and lives > 0:
			
			print("launching level "+str(level)+" with "+str(lives)+" lives")

			thislevel = Level(level, playername, lives)	
			if thislevel.outcome == 1:
				last_good_time = thislevel.final_time
				print("level passed!!")
				level+=1
			else:
				print("level failed...")
				lives -= 1						
			
		if level == 4:
			level = "WIN"
		else:
			level = "DEAD "+str(level)

		self.outcome = playername+","+level+","+last_good_time+","+str(lives)+" lives\n"




