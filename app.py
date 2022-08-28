#
# This app controls some ESC via MQTT (Homebridge IO) or a small UI
#
# Bugs and changes:
# 26.08.21 - Initial - vojj
# 27.08.21 - add StopAll and publish new values via mqtt
# 
# @author vojj
#

# import
import tkinter as tk
import tkinter.ttk as ttk

import os
import time
import threading

# my classes
from classes.class_esc_gpio import esc_gpio
from classes.eventhandler import *
from controllers.controller_motorSpeed import *
from controllers.controller_shutdown import *
from controllers.controller_mainswitch import *
from controllers.controller_mainspeed import *
from views.main import *

# global event handler
_event = None
_event = EventDispatcher()

# Init area
motor1 = esc_gpio(0, 100, 18, 50)  # GPIO18, PWM0
motor2 = esc_gpio(0, 100, 13, 50)  # GPIO18, PWM1
speed1 = Gpio(17, pigpio.INPUT)  # Input
speed2 = Gpio(18, pigpio.INPUT)  # Input
speed3 = Gpio(19, pigpio.INPUT)  # Input

# Init i/o
mainswitch1 = Controller_mainswitch(23, commandrelease=motor1.setRelease)
mainswitch2 = Controller_mainswitch(23, commandrelease=motor2.setRelease)
mainspeed1 = Controller_mainspeed(speed1, speed2, speed3, commandrelease=motor1.setSpeed)
mainspeed2 = Controller_mainspeed(speed1, speed2, speed3, commandrelease=motor2.setSpeed)

# Init homebridge values - speed
cmdMotor1Speed = controller_motorSpeed(motor1, "Speed1", "StartEngine", "SpeedAll")
cmdMotor2Speed = controller_motorSpeed(motor2, "Speed2", "StartEngine", "SpeedAll")

shutdown = controller_shutdown()

# App
app = Main("MyBoatControl", motor1, motor2)
app.mainLoop()

# end
print("Destroy all")
