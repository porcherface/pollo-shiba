######################################################################
# file: leaderboard.py
# version: 1.0.0
# author: porcherface
# descr: src for leaderboard graphics
######################################################################

import pathlib
import os
import pygame

COLOR=  (25, 255, 25)
GRAPH_PATH = pathlib.Path(__file__).parent.absolute()

# Logic level is coded here
# 1000*[max_livello_superato] + tempo rimanente in secondi
# questo funziona perfettamente se diamo meno di mille secondi per livello
# x è una stringa nome,livello max, tempo, vite, da cui estraiamo tutti i dati che
# ci servono
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

# the leader graphic handler class
class LeaderBoard:
	def __init__(self):
		# risoluzione monitor
		RES_X = 1380
		RES_Y = 1080

		self.myfont = pygame.font.SysFont('Comic Sans MS', 70)
		self.screen = pygame.display.set_mode([RES_X, RES_Y])#pygame.FULLSCREEN
		self.image = pygame.image.load(os.path.join(GRAPH_PATH,'res','leaderboard.png')).convert_alpha()
		self.rect = self.image.get_rect()

		self.datapath = os.path.join(GRAPH_PATH,'data','leaderboard_alltime.csv')

		
		f=open(self.datapath, "r")
		self.entries = f.readlines()
		
		# leaderboard sort
		self.entries.sort(key=scoreLogic)
		f.close()

		self.total = len(self.entries)
		self.passed2 = 0
		self.passed3 = 0
		for entry in self.entries:
			print(entry.strip("\n"))

			# leaderboard stats: 
			if ",WIN," in entry:
				self.passed3 += 1
				self.passed2 += 1

			if ",DEAD 3," in entry:
				self.passed2 += 1


	def draw(self):
		self.screen.blit(self.image, self.rect)
		pos_y = 200
		#top six
		for entry in self.entries[0:7]:
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

		percent2 = int(self.passed2 * 100 / self.total)
		percent3 = int(self.passed3 * 100/ self.total)
		stats1 = self.myfont.render("TOTAL ATTEMPTS: "+str(self.total)   , True, COLOR)
		stats2 = self.myfont.render("PASSED LEVEL 2: "+str(self.passed2)+" ("+ str(percent2)+"%)" , True, COLOR)
		stats3 = self.myfont.render("PASSED LEVEL 3: "+str(self.passed3)+" ("+ str(percent3)+"%)" , True, COLOR)


		self.screen.blit(stats1, stats1.get_rect().move(60, pos_y))
		self.screen.blit(stats2, stats1.get_rect().move(60, pos_y+80))
		self.screen.blit(stats3, stats1.get_rect().move(60, pos_y+160))

			
		pygame.display.flip()
		pygame.display.update()




