# msgbox.py

import pygame


class MsgBox:
	def __init__(self, playername = "porcherface"):
		self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
		self.name = self.myfont.render("player: "+playername, True, (25, 255, 25))

		self.lives3 = self.myfont.render("lives: * * *", True, (25, 255, 25))		    	
		self.lives2 = self.myfont.render("lives:   * *", True, (25, 255, 25))		    	
		self.lives1 = self.myfont.render("lives:     *", True, (25, 255, 25))		    	

	def draw(self, screen):
		self.drawName(screen)

	def drawName(self,screen):
		screen.blit(self.name,(30,100))

	def drawLives(self, screen, lives):
		if lives >= 3:		
		   	screen.blit(self.lives3,(30,150))
		if lives == 2:
		   	screen.blit(self.lives2,(30,150))
		if lives <= 1: 
		   	screen.blit(self.lives1,(30,150))

	def drawAgents(self, screen, agent_list):
			
		pos_y = 150 + 100
		num = 1
		for agent in agent_list.split(","):
			agent_status =  self.myfont.render("    s"+str(num)+" status: "+agent, True, (25, 255, 25))		    	

			screen.blit(agent_status,(30, pos_y))
			pos_y += 50
			num +=1

		if agent_list == None:
			count = "not init"
		else:
			count = agent_list.count("[OK]")
			
		self.lazors = self.myfont.render("LAZOR COUNT: "+str(count), True, (255, 25, 31))
		screen.blit(self.lazors, (30, pos_y))
