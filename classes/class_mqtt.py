#MQTT Class
import paho.mqtt.client as mqtt
import json
from types import SimpleNamespace
from classes.class_command import Command
from abc import ABC, abstractmethod

class mqtt_client():
    def __init__(self, url, path = "homebridge/from/#", service_name = "StartEngine", service_type = "Switch", characteristic = "On", command = None, port = 1883):
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe
        self.client.connect(url, port, 60)
        self.path = path
        self.client.loop_start()
        self.service_name  = service_name
        self.service_type  = service_type
        self.characteristic  = characteristic      
        self.value = 0
        #commands
        self._on_message  = command
        print("MQTT: Started")
    
    def on_subscribe(self,client, userdata, mid, granted_qos):
        print("MQTT: Subscribtion with result code "+str(granted_qos))      
    
    # The callback for when the client receives a CONNACK response from the server.
    def on_connect(self,client, userdata, flags, rc):
        print("MQTT: Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        self.client.subscribe(self.path)
    
    # The callback for when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        
        decoded = json.loads(msg.payload, object_hook=lambda d: SimpleNamespace(**d));
        if(decoded.service_name == self.service_name):
            print("MQTT:"+ str(decoded.value))
            if(decoded.characteristic == self.characteristic == "On"):  
                self.value = decoded.value
                self._on_message(bool(self.value))
            elif(decoded.characteristic == self.characteristic == "Brightness"):  
                self.value = decoded.value
                self._on_message(int(self.value))
                
    def __del__(self):
        # body of destructor
        print("MQTT:DEL Class")
       
    def destroy(self):
        # body of destructor
        print("MQTT:Destroy Class")
