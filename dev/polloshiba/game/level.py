######################################################################
# file: level.py
# version: 1.0.0
# author: porcherface
# descr: a level scene
######################################################################

# the entire logic of the game is coded here
# the first functions contain hardcoded logic 
# for levels one, two and three



import pygame
import time
from .interface import Interface
from .graphics.screen import GameScreen
import pathlib
import os

FILE_PATH = pathlib.Path(__file__).parent.absolute()

FPS = 40
clock = pygame.time.Clock()

stationif = Interface()

TIMEOUT_EVENT_KEY =  pygame.USEREVENT + 1
TRIGGER_EVENT_KEY =  pygame.USEREVENT + 2
BUTTON1_EVENT_KEY =  pygame.USEREVENT + 3
BUTTON2_EVENT_KEY =  pygame.USEREVENT + 4
START_EVENT_KEY = pygame.USEREVENT + 5
WIN_EVENT_KEY = pygame.USEREVENT + 6

TRIGGER_EVENT=pygame.event.Event(TRIGGER_EVENT_KEY)
TIMEOUT_EVENT=pygame.event.Event(TIMEOUT_EVENT_KEY)
BUTTON1_EVENT=pygame.event.Event(BUTTON1_EVENT_KEY)
BUTTON2_EVENT=pygame.event.Event(BUTTON2_EVENT_KEY)
START_EVENT=pygame.event.Event(START_EVENT_KEY)
WIN_EVENT=pygame.event.Event(WIN_EVENT_KEY)


''' 
this function contains hardcoded messages for level structures
returns an agent class for each initialized agent. if at least 1
of the agents is not correctly intialized this function returns None
'''
def InitAgents_L1():
    init_string = ""

    # hardcoded messages for level1
    print("sending init message to stations...")
    MSG_1 = "#init$S01$E01E02@"
    MSG_2 = "#init$S02$E04@"
    MSG_3 = "#init$S03$R01R02@"
    MSG_4 = "#init$S04$R04@"

    print("expecting 4 acks...")

    # send init message to stations
    stationif.send(MSG_1, 1)
    init_string += stationif.waitack(1) + ","

    stationif.send(MSG_2, 2)
    init_string += stationif.waitack(2)+ ","
    
    stationif.send(MSG_3, 3)
    init_string += stationif.waitack(3)+ ","
    
    stationif.send(MSG_4, 4)
    init_string += stationif.waitack(4)
    return init_string
def InitAgents_L2():
    init_string = ""
    
    # hardcoded messages for level2
    print("sending init message to stations...")
    MSG_1 = "#init$S01$E01E02E03@"
    MSG_2 = "#init$S02$E04@"
    MSG_3 = "#init$S03$R01R02R03@"
    MSG_4 = "#init$S04$R04@"

    print("expecting 4 acks...")

    # send init message to stations
    stationif.send(MSG_1, 1)
    init_string += stationif.waitack(1)+ ","

    stationif.send(MSG_2, 2)
    init_string += stationif.waitack(2)+ ","
    
    stationif.send(MSG_3, 3)
    init_string += stationif.waitack(3)+ ","
    
    stationif.send(MSG_4, 4)
    init_string += stationif.waitack(4)
    return init_string

def InitAgents_L3():
    init_string = ""
    
    # hardcoded messages for level3
    print("sending init message to stations...")
    MSG_1 = "#init$S01$E01E02E03@"
    MSG_2 = "#init$S02$E04E05E06@"
    MSG_3 = "#init$S03$R01R02R03@"
    MSG_4 = "#init$S04$R04R05R06@"

    print("expecting 4 acks...")

    # send init message to stations
    stationif.send(MSG_1, 1)
    init_string += stationif.waitack(1)+ ","

    stationif.send(MSG_2, 2)
    init_string += stationif.waitack(2)+ ","
    
    stationif.send(MSG_3, 3)
    init_string += stationif.waitack(3)+ ","
    
    stationif.send(MSG_4, 4)
    init_string += stationif.waitack(4)+ ","
    return init_string

class Level:
    def __init__(self, num, playername, lives):

        # preparation 

        # operator call (safety measure)
        password = ""
        while password != "polloshiba": 
            password = input("wating operator call: ")

        # logic
        print("setting room logic...")
        self.halfway = False
        self.started = False

        print("  [ OK ]")

        print("setting room state...")
        agent_list = ""
        start_time = 999.9999
        # draw graphics
        self.screen = GameScreen(playername, num, lives, start_time, agent_list)
        self.screen.setState(5)
        self.screen.draw()

        # a fake event call, just to draw graphics
        events = pygame.event.get()


        # setup stations (from hardcoded functions above)
        # 
        ready = False
        while (not ready):
            print("Initializing agents...")
            #tationif.initialize()

            
            # setting state to maintenance
            if num == 1:
                agent_list = InitAgents_L1()
            
            elif num == 2:
                print("[SKIPPED]")
                agent_list = InitAgents_L2()

            elif num == 3:
                print("[SKIPPED]")
                agent_list = InitAgents_L3()

            self.screen.term.drawAgents(agent_list)
            self.screen.draw()


            # a fake event call, just to draw graphics
            events = pygame.event.get()

            # if init is ok
            if "NA" in agent_list or "KO" in agent_list:

                time.sleep(3)
                readyinput= input("error in init, wanna go on or restart?[go/*]: ")
                if readyinput == "go":
                    ready = True
                else:
                    ready = False
            else:
                ready = True
        print(agent_list)
        print("  [ OK ]  ")

        # timeout for levels (seconds)
        if num == 1:
            start_time = 30
        if num == 2:
            start_time = 12
        if num == 3:
            start_time = 6

        self.start_time = start_time*1000
        self.timer_set = False

    
        self.screen = GameScreen(playername, num, lives, start_time, agent_list)
        # setting state
        print("setting room state...")
        self.screen.setState(0)


        print("  [ OK ]")
        print("Drawing graphics... ")
        self.screen.draw()

        print("Launching audio...")
        musicpath = os.path.join(FILE_PATH,'graphics','res','audio','portal-carolinedeleted.ogg')
        soundpath = os.path.join(FILE_PATH,'graphics','res','audio')
        
        pygame.mixer.music.load(musicpath)
        pygame.mixer.music.play()
        pygame.mixer.music.set_volume(0.3)

        self.buzzer_effect = pygame.mixer.Sound(soundpath+"/portal-buzzer.ogg")
        

        print("  [ OK ]  ")
        print("entering into exec loop...")
        out = self.execute()
        self.finalize(out)

    def execute(self):

        # events to register:
        # start button, 
        # intermediate button
        # dead!
        # timeout
        # win

        running = True
        print("\n\n -- Room is ready to use --")
        
        # the execution loop: we catch the events from here:
        # every time an event is triggered we first handle the trigger
        # then we draw

        # during the no-event routine only a portion of the assets is updated
        # to improve code security


        while running:
            events = pygame.event.get()
            for event in events:
                outcome = self.handle_events(event)
                if outcome == 1:
                    # win
                    running = False
                    return 1
                if outcome == 2:
                    # dead
                    running = False
                    return 2
                if outcome == 3:
                    # timeout
                    running = False
                    return 3

            self.screen.draw_fast()
            clock.tick(FPS) 


    # handler for events
    # for now we have
    # press s to fire a START event
    # press w to fire a WIN event
    # press D to fire a  DEAD event
    # press T to fire a TIMEOUT event
    # press M to fire a MANUAL KILL - [TO DO - WE MUST DISCUSS THIS]

    def handle_events(self, event): 

        # TIMEOUT EVENT
        if event.type == TIMEOUT_EVENT_KEY and self.timer_set:
            self.screen.setState(4)
            self.screen.timer.stop(pygame.time.get_ticks())
            self.buzzer_effect.play()

            self.screen.draw()
            time.sleep(1)
            return 3        

        # DEAD EVENT
        if event.type == TRIGGER_EVENT_KEY:
            self.screen.setState(3)
            self.screen.timer.stop(pygame.time.get_ticks())
            self.buzzer_effect.play() 
            self.screen.draw()
            time.sleep(1)
            return 2

        # BUTTON1 PRESSED
        if event.type == BUTTON1_EVENT_KEY:
            if not self.halfway and not self.started:
                pygame.event.post(START_EVENT)
                self.started = True
            if self.halfway and self.started:
                pygame.event.post(WIN_EVENT)

        # BUTTON2 PRESSED
        if event.type == BUTTON2_EVENT_KEY:
            self.halfway = True

        # START LOGIC
        if event.type == START_EVENT_KEY:
            self.screen.setState(1)

            # event timer (milliseconds)
            # event keying and registration
            TIMEOUT_EVENT = pygame.event.Event(TIMEOUT_EVENT_KEY)

            pygame.time.set_timer(TIMEOUT_EVENT_KEY, int(self.start_time))
            self.timer_set = True
            self.screen.timer.start(pygame.time.get_ticks())    
            self.screen.draw()
            return 0

        # WIN LOGIC
        if event.type == WIN_EVENT_KEY:
                self.screen.setState(2)
                self.screen.timer.stop(pygame.time.get_ticks())    
                self.screen.draw()
                time.sleep(1)
                return 1    

        # these are simulation events, just keydown press
        if event.type == pygame.KEYDOWN:

            # this is the START EVENT - we code here the first 
            # button_pressed event catcher
            if event.key == ord('s'):
                pygame.event.post(START_EVENT)

            # this is the WIN EVENT - we must code a double buttonpress logic
            if event.key == ord('w'):
                pygame.event.post(WIN_EVENT)

            # this is the DEAD catcher, we must catch a trigger from a station
            # and fire
            if event.key == ord('d'):
                pygame.event.post(TRIGGER_EVENT)

            # button pressed events sim            
            if event.key == ord('1'):
                pygame.event.post(BUTTON1_EVENT)

            if event.key == ord('2'):
                pygame.event.post(BUTTON2_EVENT)

            # MANUAL KILL SAFE ROUTINE
            if event.key == ord('m'):
                raise NotImplementedError

    # returns the time elapsed to complete the room
    # or an empty string if we died/timedout        
    def finalize(self, out):
        if out == 1:
            self.final_time = self.screen.timer.tostring()
        else:
            self.final_time = "---.---"

        time.sleep(1)
        self.outcome = out
