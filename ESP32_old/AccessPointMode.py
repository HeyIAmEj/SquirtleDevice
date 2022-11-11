import network
import time
import ujson as json
from GlobalConst import *
from Utils import *
try:
 import usocket as socket
except:
 import socket

class AccessPointMode():
    def __init__(self):
        self.ap = network.WLAN(network.AP_IF)
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        

    def get_wifi_config(self):
        print("Getting Config")
        return {"ssid":"SquirtleAP", "pass": "squirtleap"}

    def start(self):
        try:
            # get wifi config
            wifi_config = self.get_wifi_config()
            
            # start ap
            self.wifi_ap(wifi_config)
            return True
        except:
            return False

    def wifi_ap(self, wifi_config):
        self.socket.bind(('', 80))
        self.socket.listen(50)
        self.ap.active(True)
        self.ap.config(essid=wifi_config["ssid"], password=wifi_config["pass"])
        
    def endpoints(self, request):
        if(request.find(GlobalConst.SETUP_DEVICE_ENDPOINT) != -1):
            #while True:
            Utils.blinkAlert()
            response = request.split('\r\n\r\n')
            header = response[0]
            body = response[1].replace("\r\n", "")
            response_body = json.loads(body)
            print(response_body)
            saved = self.payload_save_device_config(response_body)
            if(saved):
                Utils.blinkAlert()
                Utils.blinkSuccess()
            else:
                return False
        elif(request.find(GlobalConst.SETUP_SENSOR_ENDPOINT) != -1):
            #while True:
            Utils.blinkAlert()
            response = request.split('\r\n\r\n')
            header = response[0]
            body = response[1].replace("\r\n", "")
            response_body = json.loads(body)
            print(response_body)
            saved = self.payload_save_sensor_config(response_body)
            if(saved):
                Utils.blinkAlert()
                Utils.blinkSuccess()
            else:
                return False
        elif(request.find(GlobalConst.SETUP_RESTART_ENDPOINT) != -1):
            return "restart"

        return True
    
    def payload_save_device_config(self, config):
        try:
            f = open('config.txt', 'w+')
            f.write(json.dumps(config))
            f.close()
            print("Configuração salva")
            return True
        except:
            print("Erro ao salvar configuração")
            return False

    def payload_save_sensor_config(self, config):
            try:
                f = open('sensor.txt', 'w+')
                f.write(json.dumps(config))
                f.close()
                print("Configuração salva")
                return True
            except:
                print("Erro ao salvar configuração")
                return False
    def server(self):
        try:
            conn, addr = self.socket.accept()
            print('Got a connection from %s' % str(addr))
            request = str(conn.recv(8192).decode('utf-8'))
            response_status = self.endpoints(request)
            
            if(response_status == True):
                conn.sendall('HTTP/1.1 200 OK\n')
                conn.sendall('Content-Type: text/html\n')
                conn.sendall('Connection: close\n\n')
            
            elif(response_status == "restart"):
                # RESET AUTOMATICO
                conn.sendall('HTTP/1.1 200 OK\n')
                conn.sendall('Content-Type: text/html\n')
                conn.sendall('Connection: close\n\n')
                return "restart"
            else:
                conn.sendall('HTTP/1.1 409 Conflict\n')
                conn.sendall('Content-Type: text/html\n')
                conn.sendall('Connection: close\n\n')
                    
            conn.close()
            return True
        except Exception as e:
            print(e)
            return False
