#
# This class provides a interface to control a esc.
# Bugs and changes:
# 26.08.21 - Initial - vojj
# 
#@author vojj
#

import os     #importing os library so as to communicate with the system
import time   #importing time library to make Rpi wait because its too impatient
import RPi.GPIO as GPIO
import pigpio # start pigpio on pi first!!


class esc_gpio():
    def __init__(self, min_toggle=0, max_toggle=100, esc_pin_for=13,freq=50):
        self.minPulse = 1000;
        self.maxPulse = 2000;
        self.ESC_GPIO = esc_pin_for
        self.motor = pigpio.pi()
        time.sleep(2)
        self.min_toggle = min_toggle
        self.max_toggle = max_toggle
        self.speed = self.min_toggle
        self.EStop()
        
    def EStop(self):
        self.speed = self.min_toggle
        self.motor.set_servo_pulsewidth(self.ESC_GPIO, self.getPWM(self.speed))
        
    def SoftStop(self):
        targetSpeed = self.min_toggle
        CurrentSpeed = self.speed
        self.speed = self.min_toggle
        for x in range(CurrentSpeed,targetSpeed,-1):
            self.motor.set_servo_pulsewidth(self.ESC_GPIO, self.getPWM(x))
            print("Speed:",x)
            time.sleep(0.1)
       
    def getSpeed(self):
        return self.speed
        
    def setSpeed(self,speed):
        self.speed = speed
    
    def forward(self,speed):
        if(self.inRange(speed) == True):
            self.speed = speed
            self.motor.set_servo_pulsewidth(self.ESC_GPIO, self.getPWM(self.speed))
           
    def inRange(self,speed):
        print("Speed:",speed);
        result = self.min_toggle <= speed <= self.max_toggle
        print("R:",result,"L:",self.min_toggle,"H:",self.max_toggle)
        return result
        
    def speedUp(self,speedDif):
        if(self.inRange(self.speed + speedDif) == True):
            self.speed = self.speed + speedDif
            self.motor.set_servo_pulsewidth(self.ESC_GPIO, self.getPWM(self.speed))
    
    #speed 0 .. 100%
    def getPWM(self,speed):
        timeMS = speed * self.minPulse / 100 + self.minPulse
        print("PulseWith:",timeMS);
        return timeMS
    
    def speedMax(self):
        self.speed = self.max_toggle
        self.motor.set_servo_pulsewidth(self.ESC_GPIO, self.maxPulse) # Maximum throttle.
        
    def speedMin(self):
        self.speed = self.min_toggle
        self.motor.set_servo_pulsewidth(self.ESC_GPIO, self.minPulse) # Minimum throttle.
        
    def speedDown(self,speedDif):
        if(self.inRange(self.speed - speedDif) == True):
            self.speed = self.speed - speedDif
            self.motor.set_servo_pulsewidth(self.ESC_GPIO, self.getPWM(self.speed))
        else:
            self.speed = self.min_toggle
            
    def speedZero(self):
        self.speed = 0
        self.motor.set_servo_pulsewidth(self.ESC_GPIO, self.getPWM(self.speed))
    
    def arm(self):
        self.speedZero()
        time.sleep(2)
        self.speedMin()
    
    #This is the calibration procedure of a normal ESC
    def calibrate_step1(self):   
        self.speedZero()
        print("Step1 ready: Disconnect the battery and go to next step")
    
    def calibrate_step2(self):
        self.speedMax()
        time.sleep (2)
        print("Step2 ready:Connect the battery NOW.. you will here two beeps, then wait for a gradual falling tone then go to next step")
        
    def calibrate_step3(self):
        self.speedMin()
        print ("Special tone")
        time.sleep(7)
        print ("Wait....")
        time.sleep (5)
        print ("I am processing, DONT WORRY, JUST WAIT.....")
        self.motor.set_servo_pulsewidth(self.ESC_GPIO, 0)
        time.sleep(2)
        print ("Arming ESC now...")
        self.speedMin()
        time.sleep(1)
        print ("See.... uhhhhh")
        
    def __del__(self):
        # body of destructor
        print("DEL ESC")
        #GPIO.cleanup()
       
    def destroy(self):
        # body of destructor
        print("Destroy ESC")
        #GPIO.cleanup()
