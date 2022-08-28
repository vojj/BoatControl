#
# This class provides the mqtt business logic
# get and set information via mqtt to homebridge
#
# Bugs and changes:
# 28.08.21 - Initial - vojj
# 
#@author vojj
#

#Import
import tkinter as tk
import tkinter.ttk as ttk
from functools import partial

#my classes
from classes.class_mqtt import mqtt_client


class controller_motorSpeed():
    def __init__(self, motor, nameSpeed, nameSwitch, nameSpeedAll):
        self.motor = motor
        self.motorSpeed = mqtt_client("localhost","homebridge",nameSpeed, service_type = "Lightbulb", characteristic = "Brightness", command = self.setSpeedMotor)
        self.motorSwitchOnOff = mqtt_client("localhost","homebridge",nameSwitch, command = self.startStop)
        self.motorSpeedAll = mqtt_client("localhost","homebridge",nameSpeedAll,service_type = "Lightbulb", characteristic = "Brightness", command = self.setSpeedAll)
        
        self.currentMotorSpeed = 0
        
        self.sendMotorOff()
        
    # get and set information via mqtt to homebridge
    def setSpeedMotor(self, value):
        self.currentMotorSpeed = value
        self.motor.forward(value)
    
    # puplish speed
    def sendSpeed(self, value):
        self.currentMotorSpeed = value
        self.motorSpeed.publish_value(value)
        
    # puplish of
    def sendMotorOff(self):
        self.motorSwitchOnOff.publish_value(0)
        self.motorSpeedAll.publish_value(0)
        self.sendSpeed(0)
        
    # callback function
    def startStop(self, value):
        self.sendSpeed(0)
        if(value ==  False):
            self.motor.SoftStop()
            print("Motors stopped")
        elif(value == True):
            self.motor.arm()
            print("Motors armed")
            
    #callback function
    def setSpeedAll(self, value):
        self.currentMotorSpeed = value
        self.sendSpeed(value)
        self.motor.forward(value)


