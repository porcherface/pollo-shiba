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

# paths
MAIN_PATH = pathlib.Path(__file__).parent.absolute()

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
  while "all night long":

    playername = input("player name: ")
    lives = int( input("lives: "))  
    


    result = NewGame(playername, lives, "competition")

# start a single session (player, lives, game_mode)
# but only if paghi dieci euri


