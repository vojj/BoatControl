#Import
import tkinter as tk
from functools import partial
import os
import time
import threading

#my classes
from classes.class_esc_gpio import esc_gpio
from classes.class_mqtt import mqtt_client

#Init area
motor1 = esc_gpio(0,100,18,50)
motor2 = esc_gpio(0,100,12,50)

def SetSpeedMotor1(value):
    motor1.forward(value)
    pass

cmdMotor1Switch = mqtt_client("localhost","homebridge/from/set","Speed1",service_type = "Lightbulb", characteristic = "Brightness", command = SetSpeedMotor1)

def SetSpeedMotor2(value):
    motor2.forward(value)
    pass

cmdMotor2Switch = mqtt_client("localhost","homebridge/from/set","Speed2",service_type = "Lightbulb", characteristic = "Brightness", command = SetSpeedMotor2)

def StartStopAll(value):
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


cmdMotorSwitch = mqtt_client("localhost","homebridge/from/set","StartEngine", command = StartStopAll)

#window
window = tk.Tk()
#Define hmi
bg = "black"
frameTop = tk.Frame(master=window, height=100, bg=bg)
frameTop.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frameMiddle = tk.Frame(master=window, height=50, bg="grey")
frameMiddle.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

frameMotor1 = tk.Frame(master=frameMiddle, height=50, bg=bg)
frameMotor1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
frameMotor2 = tk.Frame(master=frameMiddle, height=50, bg=bg)
frameMotor2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

frameButton = tk.Frame(master=window, height=25, bg="grey")
frameButton.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

#HMI Headline
title = tk.Label(text="--BoatControl--", master = frameTop,fg="white",bg=bg)
title.pack(fill=tk.X, side=tk.TOP,expand=True)

#HMI Motor1
label = tk.Label(text="--Motor1--", master = frameMotor1,fg="white",bg=bg)
label.pack(fill=tk.X, side=tk.TOP,expand=True)
cmdSpeedUp = partial(motor1.speedUp, 1)
button = tk.Button(text="SpeedUp", master = frameMotor1, command = cmdSpeedUp)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
cmdSpeedDown = partial(motor1.speedDown, 1)
button = tk.Button(text="SpeedDown", master = frameMotor1, command = cmdSpeedDown)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
label = tk.Label(text="--Calibration--", master = frameMotor1,fg="white",bg=bg)
label.pack(fill=tk.X, side=tk.TOP,expand=True)
button = tk.Button(text="Step One", master = frameMotor1, command = motor1.calibrate_step1)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
button = tk.Button(text="Step Two", master = frameMotor1, command = motor1.calibrate_step2)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
button = tk.Button(text="Step Three", master = frameMotor1, command = motor1.calibrate_step3)
button.pack(fill=tk.X, side=tk.TOP,expand=True)

#HMI Motor2
label = tk.Label(text="--Motor2--", master = frameMotor2,fg="white",bg=bg)
label.pack(fill=tk.X, side=tk.TOP,expand=True)
cmdSpeedUp = partial(motor2.speedUp, 1)
button = tk.Button(text="SpeedUp", master = frameMotor2, command = cmdSpeedUp)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
cmdSpeedDown = partial(motor2.speedDown, 1)
button = tk.Button(text="SpeedDown", master = frameMotor2, command = cmdSpeedDown)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
label = tk.Label(text="--Calibration--", master = frameMotor2,fg="white",bg=bg)
label.pack(fill=tk.X, side=tk.TOP,expand=True)
button = tk.Button(text="Step One", master = frameMotor2, command = motor2.calibrate_step1)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
button = tk.Button(text="Step Two", master = frameMotor2, command = motor2.calibrate_step2)
button.pack(fill=tk.X, side=tk.TOP,expand=True)
button = tk.Button(text="Step Three", master = frameMotor2, command = motor2.calibrate_step3)
button.pack(fill=tk.X, side=tk.TOP,expand=True)

#loops
window.mainloop()

#End
print("Destroy all")