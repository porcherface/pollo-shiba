######################################################################
# file: timer.py
# version: 1.0.0
# author: porcherface
# descr: src for timer graphics
######################################################################

import pygame

class Timer():
    def __init__(self):

        self.font = pygame.font.SysFont('Comic Sans MS', 32)
        counting_seconds = str(0).zfill(2)
        counting_millisecond = str(0).zfill(3)
        counting_string = "%.2s:%.3s" % ( counting_seconds, counting_millisecond)
        self.counting_text = self.font.render(str(counting_string), 1, (255,0,0))
        self.counting_rect = self.counting_text.get_rect()
        self.is_going = False
        self.start_time = 0
        self.counting_time = 0
        self.has_started = False
        self.has_stopped = False
    def position(self,x,y):
        self.counting_rect.center = (x,y)


    def start(self,start_time=pygame.time.get_ticks()):
        if not self.has_started:
            self.start_time = start_time
            self.is_going=True
            self.has_started = True

    def stop(self,stop_time=pygame.time.get_ticks()):
        if not self.has_stopped:
            self.stop_time = stop_time
            if self.is_going:
                self.counting_time = stop_time- self.start_time
            self.is_going=False
            self.has_stopped = True

    def draw(self,world):

        if self.is_going:
            self.counting_time = pygame.time.get_ticks() - self.start_time
        elif self.has_started:
            self.counting_time = self.stop_time - self.start_time
        # change milliseconds into minutes, seconds, milliseconds
        counting_seconds = str( int(( self.counting_time)/1000) ).zfill(2)
        counting_millisecond = str( self.counting_time%1000).zfill(3)
        counting_string = "%.3s . %.3s" % ( counting_seconds, counting_millisecond)
        
        self.counting_text = self.font.render(str(counting_string), 1, (255,0,0) )
        
        world.blit(self.counting_text, self.counting_rect)
