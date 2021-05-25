# button.py
import os
import pygame
import pathlib
libpath = pathlib.Path(__file__).parent.absolute()


class Agent(pygame.sprite.Sprite): 
    def __init__(self,agent_id = None):
    
        if agent_id:        
            self.image =pygame.image.load(os.path.join(libpath,agent_id,'.png')).convert_alpha()
            self.control=pygame.image.load(os.path.join(libpath,agent_id,'_ctrl.png')).convert_alpha()

            self.image.convert_alpha()  # optimise alpha
            self.image.set_colorkey(ALPHA)  # set alpha
            self.control.convert_alpha()
            self.control.set_colorkey(ALPHA)
            self.rect = self.image.get_rect()
            self.crect = self.control.get_rect()

    def draw(self, world, board):
        world.blit( self.image,self.rect) 
        board.blit( self.control, self.crect)

class Button(Agent):
    def __init__(self,icon_id=None):
        Agent.__init__(self, "button")

class Trap(pygame.sprite.Sprite):
    def __init__(self,icon_id=None):
        Agent.__init__(self, "trap")


class Emitter(pygame.sprite.Sprite):
    def __init__(self,icon_id=None):
        Agent.__init__(self, "emitter")


class Receiver(pygame.sprite.Sprite):
    def __init__(self,icon_id=None):
        Agent.__init__(self, "receiver")

        