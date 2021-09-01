#
# This class provides the mqtt business logic
# get and set information via mqtt to homebridge
#
# Bugs and changes:
# 29.08.21 - Initial - vojj
# 
#@author vojj
#

#Import
import tkinter as tk
import tkinter.ttk as ttk
import os
from functools import partial

#my classes
from classes.class_mqtt import mqtt_client

#Permission for shutdown
# Open file: sudo nano /etc/sudoers
# Append to file: pi raspberrypi =NOPASSWD: /usr/bin/systemctl poweroff

class controller_shutdown():
    def __init__(self):
        self.client = mqtt_client("localhost","homebridge","Shutdown", command = self.shutdown)
        self.client.publish_value(0)
        
    #get information via mqtt to homebridge
    def shutdown(self,value):
        if(value == True):
            os.system("systemctl poweroff")
            print("MQTT: Shutdown started")
            



