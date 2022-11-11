from GlobalConst import *
from machine import Pin, ADC
from Utils import *


class SensorInfo():
    def __init__(self):
        self.sensor1 = GlobalConst.SENSOR1
        self.sensor1_max = GlobalConst.SENSOR1_MAX_POINT
        
        self.sensor2 = GlobalConst.SENSOR2
        self.sensor2_max = GlobalConst.SENSOR2_MAX_POINT
        
        self.sensor3 = GlobalConst.SENSOR3
        self.sensor3_max = GlobalConst.SENSOR3_MAX_POINT
        
        self.sensor4 = GlobalConst.SENSOR4
        self.sensor4_max = GlobalConst.SENSOR4_MAX_POINT
        
        self.sensor5 = GlobalConst.SENSOR5
        self.sensor5_max = GlobalConst.SENSOR5_MAX_POINT
        
    def sensor1Analog(self):
        return ((ADC(self.sensor1).read() - 1024) * -1)
    def sensor2Analog(self):
        return ((ADC(self.sensor2).read() - 1024) * -1)
    def sensor3Analog(self):
        return ((ADC(self.sensor3).read() - 1024) * -1)
    def sensor4Analog(self):
        return ((ADC(self.sensor4).read() - 1024) * -1)
    def sensor5Analog(self):
        return ((ADC(self.sensor5).read() - 1024) * -1)
    
    def status(self):
        cont = 0
        while True:
            cont += 1
            print("{} - {}".format(cont, self.sensor1Analog()))
            time.sleep(1)
#         while True:
#             if(self.sensor1Analog() > GlobalConst.SENSOR1_POINT):
#                 Utils.alertLed().off()
#                 Utils.errorLed().on()
#             else:
#                 Utils.errorLed().off()
#                 Utils.alertLed().on()
#             print(self.sensor1Analog())
