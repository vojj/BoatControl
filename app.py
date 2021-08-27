#
# This app controls some ESC via MQTT (Homebridge IO) or a small UI
#
# Bugs and changes:
# 26.08.21 - Initial - vojj
# 27.08.21 - add StopAll and publish new values via mqtt
# 
#@author vojj
#

#Import
import tkinter as tk
import tkinter.ttk as ttk

from functools import partial
import os
import time
import threading

#my classes
from classes.class_esc_gpio import esc_gpio
from classes.class_mqtt import mqtt_client

#Init area
motor1 = esc_gpio(0,100,18,50) # PWM0
motor2 = esc_gpio(0,100,33,50) # PWM1

#get and set information via mqtt to homebridge
def SetSpeedMotor1(value):
    motor1.forward(value)
    pass
    
#callback function
def SetSpeedMotor2(value):
    motor2.forward(value)
    pass

cmdMotor1Speed = mqtt_client("localhost","homebridge","Speed1",service_type = "Lightbulb", characteristic = "Brightness", command = SetSpeedMotor1)
cmdMotor2Speed = mqtt_client("localhost","homebridge","Speed2",service_type = "Lightbulb", characteristic = "Brightness", command = SetSpeedMotor2)

#callback function
def SetSpeedAll(value):
    motor1.forward(value)   
    motor2.forward(value)
    cmdMotor1Speed.publish_value(value)
    cmdMotor2Speed.publish_value(value)
    pass

cmdSpeedAll = mqtt_client("localhost","homebridge","SpeedAll",service_type = "Lightbulb", characteristic = "Brightness", command = SetSpeedAll)

#callback function
def StartStopAll(value):
    cmdMotor1Speed.publish_value(0)
    cmdMotor2Speed.publish_value(0)
    cmdSpeedAll.publish_value(0)
    if(value ==  False):
        motor1.SoftStop()
        motor2.SoftStop()
        print("Motors stopped")
    elif(value == True):
        motor1.arm()
        motor2.arm()
        print("Motors armed")   
        pass
    pass


cmdMotorSwitch = mqtt_client("localhost","homebridge","StartEngine", command = StartStopAll)

#window
window = tk.Tk()
#Define hmi
bg = "black"
fg = "white"

#window basics
window.title('BoatControl')
window.geometry('600x400')

#styles
st = ttk.Style()
st.theme_use('clam')

#frames
frameTop = ttk.Frame(master=window, height=100)
frameTop.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frameMiddle = ttk.Frame(master=window, height=50)
frameMiddle.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frameMotor1 = ttk.Frame(master=frameMiddle, height=50)
frameMotor1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frameMotor2 = ttk.Frame(master=frameMiddle, height=50)
frameMotor2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frameButton = ttk.Frame(master=window, height=25)
frameButton.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

#HMI Headline
title = ttk.Label(text="--BoatControl--", master = frameTop)
title.pack(fill=tk.X, side=tk.TOP,expand=True)

#HMI Motor1
label = ttk.Label(text="--Motor1--", master = frameMotor1)
label.pack(fill=tk.X, side=tk.TOP,expand=True)
cmdSpeedUp = partial(motor1.speedUp, 1)
button = ttk.Button(text="SpeedUp", master = frameMotor1, command = cmdSpeedUp)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
cmdSpeedDown = partial(motor1.speedDown, 1)
button = ttk.Button(text="SpeedDown", master = frameMotor1, command = cmdSpeedDown)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
label = ttk.Label(text="--Calibration--", master = frameMotor1)
label.pack(fill=tk.X, side=tk.TOP,expand=True)
button = ttk.Button(text="Step One", master = frameMotor1, command = motor1.calibrate_step1)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
button = ttk.Button(text="Step Two", master = frameMotor1, command = motor1.calibrate_step2)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
button = ttk.Button(text="Step Three", master = frameMotor1, command = motor1.calibrate_step3)
button.pack(fill=tk.X, side=tk.TOP,expand=True)

#HMI Motor2
label = ttk.Label(text="--Motor2--", master = frameMotor2)
label.pack(fill=tk.X, side=tk.TOP,expand=True)
cmdSpeedUp = partial(motor2.speedUp, 1)
button = ttk.Button(text="SpeedUp", master = frameMotor2, command = cmdSpeedUp)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
cmdSpeedDown = partial(motor2.speedDown, 1)
button = ttk.Button(text="SpeedDown", master = frameMotor2, command = cmdSpeedDown)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
label = ttk.Label(text="--Calibration--", master = frameMotor2)
label.pack(fill=tk.X, side=tk.TOP,expand=True)
button = ttk.Button(text="Step One", master = frameMotor2, command = motor2.calibrate_step1)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
button = ttk.Button(text="Step Two", master = frameMotor2, command = motor2.calibrate_step2)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
button = ttk.Button(text="Step Three", master = frameMotor2, command = motor2.calibrate_step3)
button.pack(fill=tk.X, side=tk.TOP,expand=True)

#Init homebride values - speed
cmdMotor1Speed.publish_value(0)
cmdMotor2Speed.publish_value(0)
cmdSpeedAll.publish_value(0)
cmdMotorSwitch.publish_value(0)

#loops
window.mainloop()

#End
print("Destroy all")
