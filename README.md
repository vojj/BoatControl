# BoatControl
A raspberry pi project to control different ESC via an apple watch (HomeKit or others)

#Goals
* Phase1: Control two or more propellers (0.6KW to 1.2KW)
* Phase1: User want to controll speed via an apple watch
* Phase2: GPS support

#System overview
* Raspberry Pi Zero W
* 2x ESC (PWM-Control Input)
* 2x Propellers
* Current und voltage measurement of battery curcuit
* Fuses and Co.

# Software overview
* Homebridge
* Homebridge mqtt
* MQTT Broker
* Python-APP with GUI (Calibration and control)
* NodeRed flows (Setup mqtt)
* My apple watch or iphone (Control (on, off, speed))

# Setup
Install Raspberry

Install Homebridge and PlugIns

Install Broker

Install NodeRed

Install App

# Configuration
