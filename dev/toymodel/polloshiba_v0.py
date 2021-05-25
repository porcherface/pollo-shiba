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

# paths
MAIN_PATH = pathlib.Path(__file__).parent.absolute()

# inits
pygame.init()
pygame.mixer.init()

# programIcon = pygame.image.load(programIconPath)
