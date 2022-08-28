#
# This class provides the mqtt business logic
# get and set information via mqtt to homebridge
#
# Bugs and changes:
# 29.08.21 - Initial - vojj
# 
# @author vojj
#
from threading import Thread
from os import *
import time

# my classes
from classes.class_input import *
from classes.eventhandler import *


class Controller_mainspeed:

    #speed by 3 switches
    def __init__(self, speed1, speed2, speed3, commandrelease=None, event=None):

        self.speed1 = speed1
        self.speed2 = speed2
        self.speed3 = speed3

        self.oldValue = 0
        self.value = 0

        # state machine
        self.state = "Init"

        # events
        event = EventDispatcher()
        event.register("on_quit", self.on_quit)

        self._on_speed = commandrelease  # one arg 0-100%

        # Start thread
        self.runThread = True
        self.thread = Thread(None, self.run)
        self.thread.daemon = True
        self.thread.start()

    # event handler
    def on_quit(self, *args, **kwargs):
        data = kwargs.get('data')
        print('I got data from somewhere (main speed): {}'.format(data))
        self.__del__()

    # run : check input and raise command if changed
    def run(self):
        while self.runThread:
            if self.state == "Init":
                self.stateInit()
            elif self.state == "Normal":
                self.stateNormal()
            time.sleep(0.2)
    
    def stateInit(self):

        self.state = "Normal"
            
    def stateNormal(self):
        speed1 = self.speed1.read()
        speed2 = self.speed2.read()
        speed3 = self.speed3.read()

        self.value = speed1 * 30 + speed2 * 30 + speed3 * 40

        if self.oldValue != self.value:
            self._on_speed(self.value)
            self.oldValue = self.value
            print("Main speed:" + str(self.value))

    def __del__(self):
        self.runThread = False
        

