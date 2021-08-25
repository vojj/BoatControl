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
* Battery (LifePo4)

# Software overview
* Homebridge and Homebridge MQTT
* MQTT Broker
* Python-APP with GUI (Calibration and control, MQTT Client)
* Node-RED flows (Setup MQTT)
* My apple watch or iPhone (Control (on, off, speed))

# Setup
Install Raspberry Pi
* A lot of good guides you will find everywhere (https://www.raspberrypi.org)
* I am using Raspberry Pi OS with a standard image and belenaEtcher to write the SD-Card

Install Homebridge and PlugINs
* Follow this Instructions: https://github.com/homebridge/homebridge/wiki/Install-Homebridge-on-Raspbian

Install mosquitto broker via terminal
* sudo apt install mosquitto
* sudo apt install mosquitto-clients # if you need
* sudo systemctl enable mosquitto   # activate auto start
* TODO: Certification and account

Install Node-RED
* https://nodered.org/docs/getting-started/raspberrypi (for a Raspberry Pi Zero you need an other install method)

Install App

# Configuration
* Python-App

* Node-RED Flows
