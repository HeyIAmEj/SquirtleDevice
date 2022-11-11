from machine import Pin, ADC
import time
import ujson as json

class Utils:
    def successLed():
        return Pin(15, Pin.OUT)
    def alertLed():
        return Pin(4, Pin.OUT)
    def errorLed():
        return Pin(2, Pin.OUT)
    def turnOffLeds():
        Utils.successLed().off()
        Utils.alertLed().off()
        Utils.errorLed().off()
    def blinkSuccess():
        for i in range(10):
            Utils.successLed().on()
            time.sleep(0.1)
            Utils.successLed().off()
            time.sleep(0.1)
    def blinkAlert():
        for i in range(10):
            Utils.alertLed().on()
            time.sleep(0.1)
            Utils.alertLed().off()
            time.sleep(0.1)
    def blinkError():
        for i in range(10):
            Utils.errorLed().on()
            time.sleep(0.1)
            Utils.errorLed().off()
            time.sleep(0.1)
            
    def get_wifi_config():
        print("Getting Device Config")
        try:
            config_file = open("config.txt", "r")
            config = config_file.read()
            config_file.close()

            if(config != ""):
                config = json.loads(config)
                
                if(config["wifi_ssid"] != "" and config["wifi_pass"] != ""):
                    print(config)
                    return config
            return False
        except:
            return False
        
        
    def get_sensor_config():
        print("Getting Sensor Config")
        try:
            config_file = open("sensor.txt", "r")
            config = config_file.read()
            config_file.close()

            if(config != ""):
                config = json.loads(config)
                for k in config:
                    value = config[k].split(",")
                    mp = int(value[0].replace("mp:", ""))
                    pp = int(value[1].replace("pp:", ""))
                    pt = int(value[2].replace("pt:", ""))
                    config[k] = {'mp':mp, 'pp':pp, 'pt': pt}
                return config
            return {'sensor1': {'mp': 530, 'pp': 30, 'pt': 20}, 'sensor4': {'mp': 530, 'pp': 30, 'pt': 20}, 'sensor2': {'mp': 530, 'pp': 30, 'pt': 20}, 'sensor5': {'mp': 530, 'pp': 30, 'pt': 20}, 'sensor3': {'mp': 530, 'pp': 30, 'pt': 20}}
        except:
            return {'sensor1': {'mp': 530, 'pp': 30, 'pt': 20}, 'sensor4': {'mp': 530, 'pp': 30, 'pt': 20}, 'sensor2': {'mp': 530, 'pp': 30, 'pt': 20}, 'sensor5': {'mp': 530, 'pp': 30, 'pt': 20}, 'sensor3': {'mp': 530, 'pp': 30, 'pt': 20}}
        