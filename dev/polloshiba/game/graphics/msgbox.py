# msgbox.py

import pygame


class MsgBox:
    def __init__(self, playername = "porcherface"):
        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.name = self.myfont.render("player: "+playername, True, (25, 255, 25))
    	

    def draw(self, screen):
    	self.drawName(screen)

    def drawName(self,screen):
    	screen.blit(self.name,(30,100))