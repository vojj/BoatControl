# BoatControl
A raspberry pi project to control different ESC via an apple watch (Home Kit, Nest, ...)

## Warning
* This app is very new and only for testing
* Usage on your own risk

## Goals
- [x] Phase1: Control two or more propellers (0.6KW to 1.2KW)
- [x] Phase1: User want to controll speed via an apple watch
- [x] Phase1: Its working with WIFI
- [ ] Phase1: Its working with Bluetooth
- [ ] Phase2: Do control a bit more secure
- [ ] Phase3: GPS support (SpeedControl)

## System overview
* Raspberry Pi Zero W
* 2x ESC (PWM-Control Input)
* 2x Propellers
* Current und voltage measurement of battery circuit
* Fuses and Co.
* Battery (LifePo4)

# Software overview
* Homebridge and Homebridge MQTT (homebridge.io)
* MQTT Broker
* Python-APP with GUI (Calibration and control, MQTT Client)
> **pigpio** and uses a mock up class to do tests in windows env
> 
> paho.MQQT
* Node-RED flows (Setup MQTT)
* My apple watch or iPhone (Control (on, off, speed))

# Setup
## Install Raspberry Pi
* A lot of good guides you will find everywhere (https://www.raspberrypi.org)
* I am using Raspberry Pi OS with a standard image and belenaEtcher to write the SD-Card

## Install Homebridge and PlugINs
* Follow this Instructions: https://github.com/homebridge/homebridge/wiki/Install-Homebridge-on-Raspbian

## Install mosquitto broker via terminal
```
> sudo apt install mosquitto
> sudo apt install mosquitto-clients # if you need
> sudo systemctl enable mosquitto   # activate auto start
> TODO: Certification and account
```

## Install Node-RED
* https://nodered.org/docs/getting-started/raspberrypi (for a Raspberry Pi Zero you need an other install method)

## Install App
```
> git clone https://github.com/vojj/BoatControl.git
```

# Configuration
## Python-App
* Start manually or use autostart
* For the PWM-Output the pi using GPIO18 and GPIO13 (5V, GND directly from the Pi as well)
* !!! Please calibrate you ESC before usage !!!!

## Node-RED Flows and setup homebridge
* Please look into the wiki to see the Node-RED examples (https://github.com/vojj/BoatControl/wiki/Node-RED-Example).
```
> sudo systemctl enable nodered.service # Autostart Node-RED
```

## Raspberry Pi - GPIO
* Activate Remote GPIO (Raspberry Pi Configuration / Interfaces / Remote GPIO - Enable
```
> sudo pigpiod # start gpio domain, localhost
> sudo systemctl enable pigpiod # Autostart at boot
```
