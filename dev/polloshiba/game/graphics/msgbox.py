# msgbox.py

import pygame


class MsgBox:
    def __init__(self):
        # need to init this for font rendering 
        pygame.font.init() 

        self.myfont = pygame.font.SysFont('Comic Sans MS', 30)
        self.textsurface = self.myfont.render("hello msgbox", False, (25, 255, 25))

    def update(self, text = 'Some Text'):
        self.textsurface = self.myfont.render(text, False, (25, 255, 25))

    def draw(self, screen):
        screen.blit(self.textsurface,(100,100))