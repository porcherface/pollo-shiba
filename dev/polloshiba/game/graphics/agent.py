# button.py
import os
import pygame
import pathlib
libpath = pathlib.Path(__file__).parent.absolute()

class Station(pygame.sprite.Sprite):
    def __init__(self, init_string):
        pygame.sprite.Sprite.__init__(self)
        print("into station constructor: init string is" + init_string)
        if init_string != "":
            if "NA" in init_string:
                print("missing station pawn loaded")
                self.image =pygame.image.load(os.path.join(libpath,'res',"station_NA.png")).convert_alpha()
            else:
                if "#S" in init_string:
                    self.image =pygame.image.load(os.path.join(libpath,'res',"station.png")).convert_alpha()
                if "#P":
                    self.image =pygame.image.load(os.path.join(libpath,'res',"spotlight.png")).convert_alpha()
                
        else:
            self.image =pygame.image.load(os.path.join(libpath,'res',"station_NA.png")).convert_alpha()    

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

        