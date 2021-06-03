# -*- coding: utf-8 -*-

# a signature
pollo ='''
                   ▄              ▄
                  ▌▒█           ▄▀▒▌
    WOW           ▌▒▒█        ▄▀▒▒▒▐
                 ▐▄▀▒▒▀▀▀▀▄▄▄▀▒▒▒▒▒▐
               ▄▄▀▒░▒▒▒▒▒▒▒▒▒█▒▒▄█▒▐
             ▄▀▒▒▒░░░▒▒▒░░░▒▒▒▀██▀▒▌  MUCH LAZORS
            ▐▒▒▒▄▄▒▒▒▒░░░▒▒▒▒▒▒▒▀▄▒▒▌
            ▌░░▌█▀▒▒▒▒▒▄▀█▄▒▒▒▒▒▒▒█▒▐
           ▐░░░▒▒▒▒▒▒▒▒▌██▀▒▒░░░▒▒▒▀▄▌
           ▌░▒▄██▄▒▒▒▒▒▒▒▒▒░░░░░░▒▒▒▒▌
          ▌▒▀▐▄█▄█▌▄░▀▒▒░░░░░░░░░░▒▒▒▐ SUCH MAZE
          ▐▒▒▐▀▐▀▒░▄▄▒▄▒▒▒▒▒▒░▒░▒░▒▒▒▒▌
          ▐▒▒▒▀▀▄▄▒▒▒▄▒▒▒▒▒▒▒▒░▒░▒░▒▒▐
           ▌▒▒▒▒▒▒▀▀▀▒▒▒▒▒▒░▒░▒░▒░▒▒▒▌
           ▐▒▒▒▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▒▄▒▒▐
            ▀▄▒▒▒▒▒▒▒▒▒▒▒░▒░▒░▒▄▒▒▒▒▌
              ▀▄▒▒▒▒▒▒▒▒▒▒▄▄▄▀▒▒▒▒▄▀
VERY BEAMS      ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
                   ▒▒▒▒▒▒▒▒▒▒▀▀ 
'''

######################################################################
# SOFTWARE: polloshiba_v1.py
# version: 1.0.0
# author: porcherface
######################################################################

# library imports
import sys
import os
import pathlib
import pygame
import argparse
import ctypes
import serial
import threading

# polloshiba imports
from game.game import NewGame
from game.interface import Interface
from game.graphics.leaderboard import LeaderBoard

# pathings
MAIN_PATH = pathlib.Path(__file__).parent.absolute()
DATA_PATH = os.path.join(MAIN_PATH,"game", "graphics","data","leaderboard_alltime.csv")

# argument parser, to add a bunch of options for game mode 
parser = argparse.ArgumentParser()
parser.add_argument("-t","--test", help="just a pollo to test environment",action="store_true")
parser.add_argument("-d","--debug", help="debug mode for developers",action="store_true")
args = parser.parse_args()
if args.debug:
    DEBUG_MODE = True

# pygame inits
pygame.init()
pygame.mixer.init()
pygame.display.init()
pygame.font.init() 

# preloading fonts (even without using them)
# really speeds up the process during execution 
bestfont = pygame.font.SysFont('Comic Sans MS', 30)

# program icon
icon_path = os.path.join(MAIN_PATH,"game", "graphics","res","icon.png")
program_icon = pygame.image.load(icon_path)
pygame.display.set_icon(program_icon)


# station test-call
#Interface()

# MAIN CODE
if __name__ == "__main__":
  
    # everything initialized, loading pollo
    print(pollo)
    if args.test:
        sys.exit(0)


    # game loop, executes indefinitely
    while "all night long":
      
        # audio for leaderboard screen and waiting screen
        print("Launching audio...")
        musicpath = os.path.join(MAIN_PATH,'game','graphics','res','audio','portal-999999.ogg')
        pygame.mixer.music.load(musicpath)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.3)

        # load leaderboard
        leaderboard = LeaderBoard()
        leaderboard.draw()

        # false event to trigger the display flip
        events = pygame.event.get()
        
        # operator sets player properties
        if not args.debug:
            playername = input("player name: ")
            lives = int( input("lives: "))  

        else: 
            playername = "porcherface"
            lives = 3

        # if you type --quit in playername, software quits
        if playername == "--quit":
            sys.exit(0)
        
        
        # a game session
        if not args.debug:
            result = NewGame(playername, lives, "competition").outcome
        else:
            result = NewGame(playername, lives, "debug").outcome
        
        print("congrats, "+playername+". you scored: \n"+str(result))

        # save data to leaderboard file
        f=open(DATA_PATH, "a")
        f.write(result)
        f.close()


