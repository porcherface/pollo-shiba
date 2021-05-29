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
import serial
import threading

from pygame.locals import FULLSCREEN as FULLSCREEN
from entities.agent import Button,Emitter, Receiver
from entities.msgbox import MsgBox
#######
'''
things to do tomorrow: 
1) distinguish button read from emitter read.
2) add a timer and timer+button logic
3) add a blinking deadly lazor
4) add pollo shiba bottom right
5) implement lazor switch logic, which means:
   5a) implement read from arduino
   5b) implement chatbox (HUGE SHIT)
'''
#########


# paths
MAIN_PATH = pathlib.Path(__file__).parent.absolute()


# inits
pygame.init()
pygame.mixer.init()
pygame.display.init()

# program icon
programIcon = pygame.image.load(os.path.join(MAIN_PATH,"icon.png"))
pygame.display.set_icon(programIcon)




# risoluzione monitor 1
RES_X = 1380
RES_Y = 1080

world = pygame.display.set_mode([RES_X, RES_Y])

# set background masks     
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
logo = pygame.image.load(os.path.join(MAIN_PATH,'background','minilogo.png')).convert_alpha()
logo_rect = logo.get_rect().move(100,100)

FPS = 40
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

# gli agenti da mettere dentro la scena, mettiamo due pulsanti, un emitter e un receiver
a1 = Emitter()
a2 = Button()
a3 = Button()
a4 = Receiver()

a1.place(350, 430, 150, 150)
a2.place(110, 310, 250, 150)
a3.place(800, 310, 350, 150)
a4.place(350, 180, 450, 150)

agent_list = pygame.sprite.Group()
agent_list.add(a1)
agent_list.add(a2)
agent_list.add(a3)
agent_list.add(a4)

box = MsgBox()

#############################

back_4.blit(logo, logo_rect)




# some functions

# this function updates the program state (positions, activations, message board
# and other shits like these)
def update():
    box.update("ajejebrazorf")
    return 1

# this function blits everything we need to blit to screen
def render():

    back_1.blit(room, room_rect)
    beam.draw(back_1)
    for agent in agent_list:
        agent.draw(back_1, back_3)
    
    box.draw(back_2)
    world.blit(back_1, rect_1)
    world.blit(back_2, rect_2)
    world.blit(back_3, rect_3)
    world.blit(back_4, rect_4) 

    pygame.display.flip()
    pygame.display.update()
    clock.tick(FPS)

    return 1

# this function handles the events fired from the viewport
def handle_events(events):
    
    main = True
    for event in events:

        
        if event.type == pygame.QUIT:
            
            main = False
            #pygame.quit()
            #try:
            #    sys.exit()
            #finally:
            #    main = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
    
    return main


##################################################
'''
Main Loop
'''
##################################################
main = True


# SERIAL PORTS SETTINGS
port = "/dev/ttyUSB1"
baudrate = 115200 
ser = serial.Serial(port, baudrate)
data_str = ""
class Beam():
    def __init__(self):
        self.img = pygame.image.load(os.path.join(MAIN_PATH,'entities','res','beam.png')).convert_alpha()
        self.died = pygame.image.load(os.path.join(MAIN_PATH,'background','youdied.jpeg')).convert_alpha()
        self.rect = self.img.get_rect().move(360,250)
        self.state = 0
    def draw(self, screen):
        if self.state == 1:
            screen.blit(self.img, self.rect)
        if self.state == 2:
            screen.blit(self.died, self.rect)
            

beam = Beam()

# this function reads a message from station
# quando leggiamo messaggi dalla stazione dobbiamo
# fare update di map
def parseMe(data):

    #splitted = data_str.split("$")
    print("PARSED MESSAGE: ")
    #print("from: "+splitted[1])
    #print("to: "+splitted[2])
    #print("payload: "+splitted[3])
    #print("seqnum: "+splitted[4])
    #return splitted[3] == "L01_high"
    return ("HI" in data)*1 + ("TRIG" in data)*2

def readSerial():
    while True:
        #print("trying a arduino read")
        try:
            #sleep(10)
            data_str = ser.read(ser.inWaiting()).decode('ascii') #read the bytes and convert from binary array to ASCII
            if data_str != "" and data_str != " ":
                print("[DEBUG] data_str: "+data_str)  
                state = parseMe(data_str)
                print("state: "+str(state))              
                if (state == 1):
                    #print("drawing lazor")
                    beam.state = 1
                if state == 0:
                    beam.state = 0
                if state == 2:
                    beam.state = 2

        except:
            pass

thread = threading.Thread(target = readSerial)
thread.start()

while main:

    #print("events")
    update()
    render()
    main = handle_events(pygame.event.get())    
    


