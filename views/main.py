#
# This class provides the main ui
#
# Bugs and changes:
# 28.08.21 - Initial - vojj
# 
# @author vojj
#

# Import
import tkinter as tk
import tkinter.ttk as ttk
from tkinter import messagebox
from pydispatch import Dispatcher
from functools import partial
import os
import time
import threading

from views.motor_control import *


class Main(object):
    def __init__(self, title, motor1, motor2, event=None):
        # window
        self.window = tk.Tk()
        # Define hmi
        self.bg = "black"
        self.fg = "white"

        # window basics
        self.window.title(title)
        self.window.geometry('600x400')

        # events
        self.events = event

        # styles
        st = ttk.Style()
        st.theme_use('clam')

        # Start
        self.initFrames()
        self.initHead()
        self.initMotor(self.frameMotor1, "--Motor1--", motor1)
        self.initMotor(self.frameMotor2, "--Motor2--", motor2)

    def on_closing(self):
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            self.window.destroy()
            self.events.do_quit()

    def mainLoop(self):
        try:
            self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
            self.window.mainloop()
        finally:
            print("Good Bye")

    def initFrames(self):
        # frames
        self.frameTop = ttk.Frame(master=self.window, height=100)
        self.frameTop.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        self.frameMiddle = ttk.Frame(master=self.window, height=50)
        self.frameMiddle.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

        self.frameMotor1 = ttk.Frame(master=self.frameMiddle, height=50)
        self.frameMotor1.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)
        self.frameMotor2 = ttk.Frame(master=self.frameMiddle, height=50)
        self.frameMotor2.pack(fill=tk.BOTH, side=tk.LEFT, expand=True)

        self.frameButton = ttk.Frame(master=self.window, height=25)
        self.frameButton.pack(fill=tk.BOTH, side=tk.TOP, expand=True)

    def initHead(self):
        # HMI Headline
        self.title = ttk.Label(text="--BoatControl--", master=self.frameTop)
        self.title.pack(fill=tk.X, side=tk.TOP, expand=True)

    def initMotor(self, targetFrame, title, motor):
        motorControl = motor_control(targetFrame, title, motor, event=self.events)
