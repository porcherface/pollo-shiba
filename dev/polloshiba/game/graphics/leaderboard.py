######################################################################
# file: leaderboard.py
# version: 1.0.0
# author: porcherface
# descr: src for leaderboard graphics
######################################################################
'''
progetto appartamenti locali commerciali brand identity e siti web

mi occupo principalmente di interior design. penso che una corretta/giusta/studiata/
visione degli spazi e dei colori possa rendere la casa un luogo 

<< di confortevole rifugio (contrapposta a prigione da cui scappare)
>> confortevole e vivibile, invece che un rifugio da cui voler scappare   (?)

anche un dettaglio può definire (forse meglio "incidere" ?) se in quella casa vivrai bene o meno

(forse anche questa si puo ridefinire)
'''
import pathlib
import os
import pygame

COLOR=  (25, 255, 25)

GRAPH_PATH = pathlib.Path(__file__).parent.absolute()

# x è una stringa nome,livello max, tempo, vite
def scoreLogic(x):

	splitted = x.strip("\n").split(",")
	levelscore = 0
	if splitted[1] == "WIN":
		levelscore = 4000
	else:
		levelscore = int(splitted[1].split(" ")[1])*1000
	splitted[2] = splitted[2].strip(" ")
	if (splitted[2] == "---.---"):
		splitted[2] = '0'
	levelscore+=float(splitted[2])
	return -levelscore 

class LeaderBoard:
	def __init__(self):
		# risoluzione monitor 1
		RES_X = 1380
		RES_Y = 1080

		self.myfont = pygame.font.SysFont('Comic Sans MS', 70)
		self.screen = pygame.display.set_mode([RES_X, RES_Y])#pygame.FULLSCREEN
		self.image = pygame.image.load(os.path.join(GRAPH_PATH,'res','leaderboard.png')).convert_alpha()
		self.rect = self.image.get_rect()

		self.datapath = os.path.join(GRAPH_PATH,'data','leaderboard_alltime.csv')

		
		f=open(self.datapath, "r")
		self.entries = f.readlines()
		self.entries.sort(key=scoreLogic)
		f.close()

		# leaderboard sort

		for entry in self.entries:
			print(entry.strip("\n"))



	def draw(self):
		self.screen.blit(self.image, self.rect)
		pos_y = 200
		for entry in self.entries:
			splitted = entry.strip("\n").split(",")
			if len(splitted) < 3 :
				print("ERROR IN LEADERBOARD FORMATTING")
			name = self.myfont.render(splitted[0], True, COLOR )	
			last_level = self.myfont.render(splitted[1], True, COLOR )	
			time =  self.myfont.render(splitted[2], True, COLOR )	
			lives = self.myfont.render(splitted[3], True, COLOR)

			self.screen.blit(name, name.get_rect().move(60, pos_y))
			self.screen.blit(last_level, last_level.get_rect().move(700, pos_y))
			self.screen.blit(time, time.get_rect().move(1080, pos_y))
			
			pos_y += 80


		pygame.display.flip()
		pygame.display.update()




