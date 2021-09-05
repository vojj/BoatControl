#
# This class provides a interface to control a gpio.
# Bugs and changes:
# 05.09.21 - Initial - vojj
# 
#@author vojj
#

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
import pigpio # start pigpio on pi first!!


class Gpio:
    def __init__(self,  pin=13, direction=pigpio.INPUT):  # BCM GPIO13

        self.pin = pin
        self.pi = pigpio.pi()       # pi1 accesses the local Pi's GPIO
        self.pi.set_mode(self.pin, direction)  # GPIO  4 as input
        self.pi.read(self.pin)  # get level of dick's GPIO 4

    def read(self):
        return self.pi.read(self.pin)

    def write(self, value: bool):
        return self.pi.write(self.pin, value)

    def __del__(self):
        # body of destructor
        print("DEL gpio")

    def destroy(self):
        # body of destructor
        print("Destroy GPIO")
