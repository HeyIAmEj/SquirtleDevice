# import urequests as requests
from urequests import *
import ujson
from SensorInfo import *
from StationMode import *
from Utils import *

class PayloadSensor():
    def __init__(self):
        config = Utils.get_wifi_config()
        self.device_id = config["device_id"]
        self.client_id = config["client_id"]
        self.status = config["status"]
        self.sensor1 = "0.0"
        self.sensor2 = "0.0"
        self.sensor3 = "0.0"
        self.sensor4 = "0.0"
        self.sensor5 = "0.0"
        
    def prepare_payload(self):
        sensor_payload = { 
          "device_id": self.device_id,
          "client_id": self.client_id,
          "status": self.status,
          "sensor1" : self.sensor1,
          "sensor2" : self.sensor2,
          "sensor3" : self.sensor3,
          "sensor4" : self.sensor4,
          "sensor5" : self.sensor5,
        }
        json_object = ujson.dumps(sensor_payload)
        return json_object
    
    def get_sensors_info(self):
        sensorinfo = SensorInfo()
        
        self.sensor1 = str(sensorinfo.sensor1Analog())
        print("Sensor 1: "+self.sensor1)
        
        self.sensor2 = str(sensorinfo.sensor2Analog())
        print("Sensor 2: "+self.sensor2)

        self.sensor3 = str(sensorinfo.sensor3Analog())
        print("Sensor 3: "+self.sensor3)

        self.sensor4 = str(sensorinfo.sensor4Analog())
        print("Sensor 4: "+self.sensor4)

        self.sensor5 = str(sensorinfo.sensor5Analog())
        print("Sensor 5: "+self.sensor5)

        
    def send(self):
        # obtem informacoes dos sensores
        self.get_sensors_info()
        
        #prepara o payload
        data = self.prepare_payload()
                
        # realiza envio do payload
        header_data = { "content-type": 'application/json; charset=utf-8', "devicetype": '1'}
        endpoint = 'https://squirtleapi.herokuapp.com/api/v1/dispositivo/{}/sensores'.format(self.device_id)
        response = request("PUT", endpoint, headers = header_data, data=data)
        
        
        response_json = ujson.loads(response.content)
        print(response_json)
