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
from views.main import *

# Event handler
event = eventhandler()

# Init area
motor1 = esc_gpio(0, 100, 18, 50, event=event)  # GPIO18, PWM0
motor2 = esc_gpio(0, 100, 13, 50, event=event)  # GPIO18, PWM1

# Init i/o
mainswitch1 = Controller_mainswitch(23, commandrelease=motor1.setRelease)
mainswitch2 = Controller_mainswitch(23, commandrelease=motor2.setRelease)

# Init homebridge values - speed
cmdMotor1Speed = controller_motorSpeed(motor1, "Speed1", "StartEngine", "SpeedAll")
cmdMotor2Speed = controller_motorSpeed(motor2, "Speed2", "StartEngine", "SpeedAll")

shutdown = controller_shutdown()

# App
app = Main("MyBoatControl", motor1, motor2, event=event)
app.mainLoop()

# end
print("Destroy all")
