#
# This class provides the mqtt business logic
# get and set information via mqtt to homebridge
#
# Bugs and changes:
# 29.08.21 - Initial - vojj
# 
# @author vojj
#
import threading
from threading import *
from os import *
from time import *

# my classes
from classes.class_input import *


class Controller_mainswitch:
    def __init__(self, pin=13, commandrelease=None):
        self.pin = pin
        self.input = Input(self.pin)
        self.value = self.input.read()
        self.oldValue = False

        self._on_release = commandrelease  # one arg 0 = no release  1 = release

        # Start thread
        self.thread = threading.Thread(self.run)
        self.thread.run()

    # run : check input and raise command if changed
    def run(self):
        while True:
            self.value = self.input.read()
            if self.oldValue != self.value:
                self._on_release(self.value)
                self.oldValue = self.value
                print("Main switch:" + self.value)
            time.sleep(0.2)


