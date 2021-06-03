######################################################################
# file: game.py
# version: 1.0.0
# author: porcherface
# descr: handles a game session, acts as manager for scenes and levels
######################################################################

# this file contains game logic loop. very simple
# this will be more consistent when we'll have more game modes to add
# for now raises an error every time game-mode is not "competition"

# competition mode has:
#   no live laser view, 
#   no control board
#   no randomness

from .level import Level
from .graphics.screen import GameScreen

class NewGame:
	def __init__(self, playername, lives, gamemode):
		if gamemode != "competition" and gamemode != "debug":
			raise NotImplementedError

		# handshake with player
		print("***********************")
		print("hello " + playername)
		print("you have "+str(lives)+" lives")
		print("***********************")
		
		level = 1	
		# a very rudimental input check
		if type(lives) != type(5):
			print("something wrong with input, setting to 1")
		if lives < 0 or lives > 3:
			print("too many lives, baby, setting to 1")
			lives = 1
		
		# levels loop: 
		last_good_time = "---.---"
		while level <= 3 and lives > 0:
			
			print("launching level "+str(level)+" with "+str(lives)+" lives")
			thislevel = Level(level, playername, lives, gamemode)	
			
			# if we win the level
			if thislevel.outcome == 1:
				last_good_time = thislevel.final_time
				print("level passed!!")
				level+=1
			# if we lose the level
			else:
				print("level failed...")
				lives -= 1	

		# this is the last level played (either if we won or lost)
		# we passed 3 levels	
		if level == 4:
			level = "WIN"
		# we died on a level
		else:
			level = "DEAD "+str(level)

		# a big string containing all the information about the game session
		# we have just played
		self.outcome = playername+","+level+","+last_good_time+","+str(lives)+" lives\n"




