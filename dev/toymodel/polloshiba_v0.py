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

FPS = 40
# inits
pygame.init()
pygame.mixer.init()
pygame.display.init()

# program icon
# programIcon = pygame.image.load(programIconPath)



# qui metto la pianta
#backdroppath=os.path.join(labyrinthpath,'res','bg_maze.png')
#backdrop = pygame.image.load(os.path.join(backdroppath)).convert_alpha()
#backdropbox = backdrop.get_rect()

# risoluzione monitor 1
RES_X = 1380
RES_Y = 1080

world = pygame.display.set_mode([RES_X, RES_Y])

        
back_1 = pygame.image.load(os.path.join(MAIN_PATH,'background','map.png')).convert_alpha()
back_2 = pygame.image.load(os.path.join(MAIN_PATH,'background','term.png')).convert_alpha()
back_3 = pygame.image.load(os.path.join(MAIN_PATH,'background','control.png')).convert_alpha()
back_4 = pygame.image.load(os.path.join(MAIN_PATH,'background','doge.png')).convert_alpha()

rect_1 = back_1.get_rect().move(0, 0)
rect_2 = back_2.get_rect().move(1000, 0)
rect_3 = back_3.get_rect().move(0, 700)
rect_4 = back_4.get_rect().move(1000, 700)

room = pygame.image.load(os.path.join(MAIN_PATH, 'background', 'room.png')).convert_alpha()
room_rect = room.get_rect().move(50,150)


back_1.blit(room, room_rect)
world.blit(back_1, rect_1)
world.blit(back_2, rect_2)
world.blit(back_3, rect_3)
world.blit(back_4, rect_4) 

clock = pygame.time.Clock()


''' ui concept: 

*************************************************************************************************
*                                                                *                              *
*                                                                *                              *
*   room - pianta della stanza                                   *  msgboard                    *
*   1000 x 700                                                   *  380 x 700                   *
*                                                                *                              *
*   sfondo bianco, ci inserisco una pianta della stanza          *  sfondo nero                 *
*   siccome la pianta per ora manca, ci ficco dentro un          *  ci metto dentro un terminal *
*   rettangolo con dei finti muri e buonanotte                   *  in stile hacker             *
*                                                                *                              *
*                                                                *                              *
*                                                                *                              *
*                                                                *                              *
*                                                                *                              *
*                                                                *                              *
*                                                                *                              *
*************************************************************************************************
*                                                                *                              *
*    1000 x 380                                                  *  380 x 380                   *
*    sfondo grigio, una specie di banco dei bottoni. ci          *  un logo con un pollo shiba  *
*    metterò dentro i comandi di laser, pulsanti e cazzi vari    *  e magari quache tasto tipo  *
*                                                                *  QUIT o roba cosi            *
*                                                                *                              *
*************************************************************************************************
'''

# gli agenti da mettere dentro la scena, mettiamo un pulsante un emitter una trap e un receiver
agent_list = pygame.sprite.Group()
#agent_list.add()


# some functions

# this function updates the program state (positions, activations, message board
# and other shits like these)
def update():
    return 1

# this function blits everything we need to blit to screen
def render():
    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)
    return 1

# this function handles the events fired from the viewport
def handle_events(events):
    
    main = True
    for event in events:
        if event.type == pygame.QUIT:
            pygame.quit()
            try:
                sys.exit()
            finally:
                main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    
    return main

'''
Main Loop
'''
main = True
while main:

    #print("events")
    update()
    render()
    main = handle_events(pygame.event.get())    
    


