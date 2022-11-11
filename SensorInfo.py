from GlobalConst import *
from machine import Pin, ADC
from Utils import *


class SensorInfo():
    def __init__(self):
        self.bits = 4095
        self.sensor1 = GlobalConst.SENSOR1
        #self.sensor1_max = GlobalConst.SENSOR1_MAX_POINT
        
        self.sensor2 = GlobalConst.SENSOR2
        #self.sensor2_max = GlobalConst.SENSOR2_MAX_POINT
        
        self.sensor3 = GlobalConst.SENSOR3
        #self.sensor3_max = GlobalConst.SENSOR3_MAX_POINT
        
        self.sensor4 = GlobalConst.SENSOR4
        #self.sensor4_max = GlobalConst.SENSOR4_MAX_POINT
        
        self.sensor5 = GlobalConst.SENSOR5
        #self.sensor5_max = GlobalConst.SENSOR5_MAX_POINT
        
    def sensor1Analog(self):
        print("Obtendo informação do sensor 1")
        sensor1 = ADC(Pin(self.sensor1))
        sensor1.atten(ADC.ATTN_11DB)
        return (sensor1.read() - self.bits) * -1
    def sensor2Analog(self):
        print("Obtendo informação do sensor 2")
        sensor2 = ADC(Pin(self.sensor2))
        sensor2.atten(ADC.ATTN_11DB)
        return (sensor2.read() - self.bits) * -1
    def sensor3Analog(self):
        print("Obtendo informação do sensor 3")
#         sensor3 = ADC(Pin(self.sensor3))
#         sensor3.atten(ADC.ATTN_11DB)
#         return (sensor3.read() - self.bits) * -1
        return "0"
    def sensor4Analog(self):
        print("Obtendo informação do sensor 4")
#         sensor4 = ADC(Pin(self.sensor4))
#         sensor4.atten(ADC.ATTN_11DB)
#         return (sensor4.read() - self.bits) * -1
        return "0"
    def sensor5Analog(self):
        print("Obtendo informação do sensor 5")
#         sensor5 = ADC(Pin(self.sensor5))
#         sensor5.atten(ADC.ATTN_11DB)
#         return (sensor5.read() - self.bits) * -1
        return "0"
    
    
    def status(self):
        cont = 0
        while True:
            cont += 1
            print("Sensor 1 | {}".format(self.sensor1Analog()))
            print("Sensor 2 | {}".format(self.sensor2Analog()))
            time.sleep(1)