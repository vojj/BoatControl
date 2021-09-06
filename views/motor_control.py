#
# This class provides the motor control ui
#
# Bugs and changes:
# 28.08.21 - Initial - vojj
# 
#@author vojj
#

#Import
import tkinter as tk
import tkinter.ttk as ttk
from threading import Thread
import time
from functools import partial

class motor_control():
    def __init__(self, targetFrame, title, motor):
        self.targetFrame = targetFrame
        self.motor = motor
        #HMI Motor1
        label = ttk.Label(text="--" + title + "--", master=self.targetFrame)
        label.pack(fill=tk.X, side=tk.TOP, expand=True)
        
        # scale
        self.scaleMotorSpeed = 0
        self.scaleMotor1 = None
        self.initScale(self.targetFrame)

        # Init
        self.labelStatusRelease = None
        self.labelMotorSpeed = None
        self.initControl(self.targetFrame, self.motor)

        # refresh thread
        self.threadRefresh = Thread(None, self.refreshControls)
        self.threadRefresh.start()

        
    def refreshControls(self):
        while True:
            self.updateMotorSpeed()
            self.updateLabels()
            time.sleep(0.3)
        
    def setMotorSpeed(self, value):
        if self.scaleMotorSpeed != int(float(value)):
            self.motor.forward(int(float(value)))
            self.scaleMotorSpeed = int(float(value))
            
    def initScale(self, frame):
        self.scaleMotor1 = ttk.Scale(command=self.setMotorSpeed, master=frame, from_=0, to=100, orient=tk.HORIZONTAL)
        self.scaleMotor1.pack(fill=tk.X, side=tk.TOP, expand=True)

    # refresh scale
    def updateMotorSpeed(self):
            value = self.motor.getSpeed()
            if self.scaleMotorSpeed != value:
                self.scaleMotor1.set(self.scaleMotorSpeed)

    def updateLabels(self):
        release = self.motor.getRelease()
        speed = self.motor.getSpeed()
        if release:
            self.labelStatusRelease.config(background="green")
        else:
            self.labelStatusRelease.config(background="red")
        self.labelMotorSpeed.config(text=" " + str(speed) + " ")

    def initReleaseStatus(self, frame):
        self.labelStatusRelease = ttk.Label(text="  R  ", master=frame)
        self.labelStatusRelease.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    def initLabelMotorSpeed(self, frame):
        self.labelMotorSpeed = ttk.Label(text="  S  ", master=frame)
        self.labelMotorSpeed.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

    def initControl(self, frame, motor):

        frameTop = ttk.Frame(master=frame, height=50)
        frameTop.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        frameMiddle = ttk.Frame(master=frame, height=50)
        frameMiddle.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        frameButtom = ttk.Frame(master=frame, height=50)
        frameButtom.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        cmdSpeedUp = partial(motor.speedUp, 1)
        button = ttk.Button(text="SpeedUp", master=frameTop, command=cmdSpeedUp)
        button.pack(fill=tk.X, side=tk.TOP, expand=True)

        cmdSpeedDown = partial(motor.speedDown, 1)
        button = ttk.Button(text="SpeedDown", master=frameTop, command=cmdSpeedDown)
        button.pack(fill=tk.X, side=tk.TOP, expand=True)

        button = ttk.Button(text="Arm", master=frameTop, command=motor.arm)
        button.pack(fill=tk.X, side=tk.TOP, expand=True)

        self.initReleaseStatus(frameMiddle)
        self.initLabelMotorSpeed(frameMiddle)

        button = ttk.Button(text="Stop", master=frameButtom, command=motor.SoftStop)
        button.pack(fill=tk.X, side=tk.TOP, expand=True)

        label = ttk.Label(text="--Calibration--", master=frameButtom)
        label.pack(fill=tk.X, side=tk.TOP, expand=True)

        button = ttk.Button(text="Step One", master=frameButtom, command=motor.calibrate_step1)
        button.pack(fill=tk.X, side=tk.TOP, expand=True)

        button = ttk.Button(text="Step Two", master=frameButtom, command=motor.calibrate_step2)
        button.pack(fill=tk.X, side=tk.TOP, expand=True)

        button = ttk.Button(text="Step Three", master=frameButtom, command=motor.calibrate_step3)
        button.pack(fill=tk.X, side=tk.TOP, expand=True)
 