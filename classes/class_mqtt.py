#
# This class provides a interface via mqtt and connects to a mqqt broker.
# * It subscribes to a path and filters the message is given from homebridge io
# Bugs and changes:
# 26.08.21 - Initial - vojj
# 27.08.21 - add publish
# 
#@author vojj
#

import paho.mqtt.client as mqtt
import json
from types import SimpleNamespace
from threading import Thread
from abc import ABC, abstractmethod

class mqtt_client():
    def __init__(self, url, path="homebridge/from/#", service_name="StartEngine", service_type="Switch", characteristic="On", command=None, port=1883):
        # Init fields
        self.value = 0
        self.name = service_name
        self.service_name = service_name
        self.service_type = service_type
        self.characteristic = characteristic
        # Init client
        self.path_from = path + "/from/set"  # read from homebridge
        self.path_to = path + "/to/set"  # write to homebridge
        self.client = mqtt.Client()
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.on_subscribe = self.on_subscribe
        self.client.on_publish = self.on_publish
        # do connect async
        thread = Thread(None, self.connect, args=(url, port, 30))
        thread.start()
        # start loop
        self.client.loop_start()
        # commands
        self._on_message = command  # delegate or function, _on_message(value)
        print("MQTT " + self.service_name + ": Started")

    def connect(self, url, port, timeout):
        try:
            self.client.connect(url, port, timeout)
        except Exception:
            print("MQTT: Connection Error")

    def publish_value(self, value):
        # Example payload: {"name":"SpeedAll","characteristic":"On","value":true}
        payload = homebridge_payload_set(value=value, name=self.name, service_name=self.service_name, service_type=self.service_type, characteristic=self.characteristic)
        payload_json = json.dumps(payload.__dict__)
        self.client.publish(self.path_to, payload_json)
        
    def on_subscribe(self,client, userdata, mid, granted_qos):
        print("MQTT "+ self.service_name +": Subscribtion with result code "+str(granted_qos))
        
    # The callback for when the client receives a CONNACK response from the server.
    def on_publish(self,client, userdata, rc):
        print("MQTT "+ self.service_name +": Published with result code "+str(rc))
        
    # The callback when the client receives a CONNACK response from the server.
    def on_connect(self,client, userdata, flags, rc):
        print("MQTT "+ self.service_name +": Connected with result code "+str(rc))
        # Subscribing in on_connect() means that if we lose the connection and
        # reconnect then subscriptions will be renewed.
        self.client.subscribe(self.path_from)
    
    # The callback when a PUBLISH message is received from the server.
    def on_message(self, client, userdata, msg):
        decoded = json.loads(msg.payload, object_hook=lambda d: SimpleNamespace(**d));
        if(decoded.service_name == self.service_name):
            print("MQTT "+ self.service_name +":"+ str(decoded.value))
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

#Class to serilize with json
class homebridge_payload_set:
  def __init__(self, value, name = "lamp", service_name = "light", service_type = "Lightbulb", characteristic = "On"):
    self.name = name
    self.service_name = service_name
    self.service_type = service_type
    self.characteristic = characteristic
    self.value = value
