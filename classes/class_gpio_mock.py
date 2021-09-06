#
# This class provides a interface to mock gpio.
# Bugs and changes:
# 05.09.21 - Initial - vojj
#
#@author vojj
#

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient


class Gpio_mock(object):
    def __init__(self,  pin=13, direction=0):  # BCM GPIO13
        self.pin = pin
        self.value = False
        # self.pi = pigpio.pi()       # pi1 accesses the local Pi's GPIO
        # self.pi.set_mode(self.pin, direction)  # GPIO  4 as input
        # self.pi.read(self.pin)  # get level of dick's GPIO 4

    def read(self, pin):
        return self.value

    def write(self, value: bool):
        self.value = value

    @staticmethod
    def pi():
        return Gpio_mock()

    def set_servo_pulsewidth(self, pin, pwm):
        return 0

    def set_mode(self, pin, mode):
        return 0

    def INPUT(self):
        return 0

    def __del__(self):
        # body of destructor
        print("DEL gpio mock")

    def destroy(self):
        # body of destructor
        print("Destroy GPIO mock")
