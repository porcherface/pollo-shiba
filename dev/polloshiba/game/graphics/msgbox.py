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