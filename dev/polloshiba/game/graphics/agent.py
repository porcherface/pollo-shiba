# button.py
import os
import pygame
import pathlib
libpath = pathlib.Path(__file__).parent.absolute()


class Agent(pygame.sprite.Sprite): 
    def __init__(self,agent_id = None):
        pygame.sprite.Sprite.__init__(self)
        self.state = 0
        if agent_id:        
            
            self.image =pygame.image.load(os.path.join(libpath,'res',agent_id+'.png')).convert_alpha()

            self.cmdimg = []
            #self.control=pygame.image.load(os.path.join(libpath,'res',agent_id+'_ctrl.png')).convert_alpha()
            self.cmdimg.append(pygame.image.load(os.path.join(libpath,'res','on.png')).convert_alpha() )
            self.cmdimg.append(pygame.image.load(os.path.join(libpath,'res','off.png')).convert_alpha() )


            #self.image.set_colorkey(ALPHA)  # set alpha
            #self.cmdimg[0].set_colorkey(ALPHA)
            #self.cmdimg[1].set_colorkey(ALPHA)
            
            self.rect = self.image.get_rect()
            self.crect = self.cmdimg[0].get_rect()

    def place(self,xm, ym, xc,yc):
    
        self.rect.move_ip(xm,ym)
        self.crect.move_ip(xc,yc)


    def draw(self, board, ctrl):
        board.blit( self.image,self.rect) 
        ctrl.blit( self.cmdimg[self.state], self.crect)

    def update(self):
        pass

class Button(Agent):
    def __init__(self,icon_id="button"):
        Agent.__init__(self, "button")

class Trap(Agent):
    def __init__(self,icon_id="trap"):
        Agent.__init__(self, "trap")


class Emitter(Agent):
    def __init__(self,icon_id="emitter"):
        Agent.__init__(self, "emitter")


class Receiver(Agent):
    def __init__(self,icon_id="receiver"):
        Agent.__init__(self, "receiver")

        