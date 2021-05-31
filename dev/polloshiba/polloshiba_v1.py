# -*- coding: utf-8 -*-
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
  VERY BEAMS    ▀▄▄▄▄▄▄▀▀▀▒▒▒▒▒▄▄▀
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
from game.game import NewGame
from game.interface import Interface

from game.graphics.leaderboard import LeaderBoard
# paths
MAIN_PATH = pathlib.Path(__file__).parent.absolute()
DATA_PATH = os.path.join(MAIN_PATH,"game", "graphics","data","leaderboard_alltime.csv")


parser = argparse.ArgumentParser()

parser.add_argument("-t","--test", help="just a pollo to test environment",action="store_true")
parser.add_argument("-d","--debug", help="debug mode for developers",action="store_true")

args = parser.parse_args()

if args.debug:
    DEBUG_MODE = True

# inits
pygame.init()
pygame.mixer.init()
pygame.display.init()
pygame.font.init() 

# preloading fonts really speeds up the process during execution (LOL)
bestfont = pygame.font.SysFont('Comic Sans MS', 30)

# program icon
icon_path = os.path.join(MAIN_PATH,"game", "graphics","res","icon.png")
program_icon = pygame.image.load(icon_path)
pygame.display.set_icon(program_icon)


# station test-call
#Interface()

# MAIN CODE
if __name__ == "__main__":
  print(pollo)
  if args.test:
    sys.exit(0)



  while "all night long":
    
    print("Launching audio...")
    musicpath = os.path.join(MAIN_PATH,'game','graphics','res','audio','portal-999999.mp3')
    pygame.mixer.music.load(musicpath)
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.3)


    leaderboard = LeaderBoard()
    leaderboard.draw()
    events = pygame.event.get()
    
    playername = input("player name: ")
    lives = int( input("lives: "))  
    

    result = NewGame(playername, lives, "competition").outcome

    print("congrats, "+playername+". you scored: "+str(result))

    f=open(DATA_PATH, "a")
    f.write(result)
    f.close()
# start a single session (player, lives, game_mode)
# but only if paghi dieci euri


