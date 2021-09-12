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


class Controller_mainswitch:
    def __init__(self, pin=13, commandrelease=None, event=None):
        self.pin = pin
        self.input = Input(self.pin)
        self.value = self.input.read()
        self.oldValue = False
        
        # state machine
        self.state = "Init"

        # events
        event = EventDispatcher()
        event.register("on_quit", self.on_quit)

        self._on_release = commandrelease  # one arg 0 = no release  1 = release

        # Start thread
        self.runThread = True
        self.thread = Thread(None, self.run)
        self.thread.daemon = True
        self.thread.start()

    # event handler
    def on_quit(self, *args, **kwargs):
        data = kwargs.get('data')
        print('I got data from somewhere (main switch): {}'.format(data))
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
        self.value = self.input.read()
        if not self.value:
            self.state = "Normal"
        else:
            print("Main switch: shut down first")
            time.sleep(1)
            
    def stateNormal(self):
        self.value = self.input.read()
        if self.oldValue != self.value:
            self._on_release(self.value)
            self.oldValue = self.value
            print("Main switch:" + str(self.value))

    def __del__(self):
        self.runThread = False
        

