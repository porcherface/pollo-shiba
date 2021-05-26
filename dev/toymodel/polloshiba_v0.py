# polloshiba_v0.py

try:    
    import pygame  
except:
    print("installa pygame, cazzone")


# imports
import sys
import os
import pathlib
import argparse
import ctypes

from pygame.locals import FULLSCREEN as FULLSCREEN
import entities.agent

# paths
MAIN_PATH = pathlib.Path(__file__).parent.absolute()

# inits
pygame.init()
pygame.mixer.init()

# program icon
# programIcon = pygame.image.load(programIconPath)



# qui metto la pianta
#backdroppath=os.path.join(labyrinthpath,'res','bg_maze.png')
#backdrop = pygame.image.load(os.path.join(backdroppath)).convert_alpha()
#backdropbox = backdrop.get_rect()

# risoluzione monitor 1
RES_X = 1280
RES_Y = 1080

world = pygame.display
screen = pygame.display

world.set_mode([RES_X, RES_Y])
#screen.set_mode([RES_X, RES_Y])
# gli agenti da mettere dentro la scena, mettiamo un pulsante un emitter una trap e un receiver

agent_list = pygame.sprite.Group()
#agent_list.add()
        

''' ui concept: 

**************************************************************************************************
*                                                                 *                              *
*                                                                 *                              *
*   room - pianta della stanza                                    *  msgboard                    *
*   1000 x 700                                                    *  380 x 700                   *
*                                                                 *                              *
*   sfondo bianco, ci inserisco una pianta della stanza           *  sfondo nero                 *
*   siccome la pianta per ora manca, ci ficco dentro un           *  ci metto dentro un terminal *
*   rettangolo con dei finti muri e buonanotte                    *  in stile hacker             *
*                                                                 *                              *
*                                                                 *                              *
*                                                                 *                              *
*                                                                 *                              *
*                                                                 *                              *
*                                                                 *                              *
*                                                                 *                              *
*                                                                 *                              *
*                                                                 *                              *
*                                                                 *                              *
*                                                                 *                              *
**************************************************************************************************
*                                                                 *                              *
*    1000 x 280                                                   *  380 x 280                   *
*    sfondo grigio, una specie di banco dei bottoni. ci           *  un logo con un pollo shiba  *
*    metterò dentro i comandi di laser, pulsanti e cazzi vari     *  e magari quache tasto tipo  *
*                                                                 *  QUIT o roba cosi            *
*                                                                 *                              *
**************************************************************************************************
'''



'''

# some functions
def render(self):
    pass

def update(self):
    pass

def handle_events(self, events):
    
    main = True

    for event in events:

        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False
        if event.type == pygame.KEYDOWN:

            self.respawn_bugfix = True
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                try:
                    sys.exit()
                finally:
                    main = False


            if event.key == ord('a'):
                self.player1.control(-steps1, 0)
            if event.key == pygame.K_LEFT:
                self.player2.control(-steps2, 0)
            
            if event.key == ord('e'):
                self.player1.showchat(1)
                
            if event.key == ord('f'):
                self.focused_player = self.player1

        return main

'''

'''
Main Loop
'''
main = True
while main:
    #main = self.handle_events(pygame.event.get())    
    #main = self.update()
    #self.render()
    #main = self.reunite()



    pass

