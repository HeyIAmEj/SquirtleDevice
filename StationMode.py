import network
import time
import os
import ujson as json

class StationMode():
    def __init__(self):
        self.station = network.WLAN(network.STA_IF)
        self.station.active(True) 

    def get_wifi_config(self):
        print("Getting Config")
        try:
            config_file = open("config.txt", "r")
            config = config_file.read()
            print(config)
            config_file.close()

            if(config != ""):
                config = json.loads(config)
                if(config["wifi_ssid"] != "" and config["wifi_pass"] != ""):
                    print(config)
                    return config

            return False
        except:
            return False
    
    def check(self, scanned_wifi, ssid):
        for x in scanned_wifi:
            print("Wifi:{}".format(x[0]))
        for x in scanned_wifi:
            print (b"{}".format(ssid) in x[0])
            if b"{}".format(ssid) in x[0]: return True
        return False

    def start(self):
        # faz o scan de redes proximas
        print("Start scanner")
        scanned_wifi = self.scan()
        print("Scanned!")
        # pega informacoes da rede para se conectar
        wifi_config = self.get_wifi_config()
        if(wifi_config == False):
            print("Erro ao obter informações de configuração")
            return False
        else:
            # checa se está disponível
            isAvailable = self.check(scanned_wifi, wifi_config["wifi_ssid"])
            print("isAvailable: ", isAvailable)
            if(isAvailable):
                isConnected = self.connect(wifi_config)
                if isConnected : return True
                else: return False
            else:
                print("Algo deu errado!")
                return False
        
    def scan(self):
        print("Verificando Redes Wifi Próximas")
        return self.station.scan()
        
    def connect(self, wifi_config):
        print("Tentativa de Conexão")
        station = self.station
        
        if(station.isconnected()):
            print("entrou is connected")
            return True
        else:
            print("Conectando...")
            station.connect(wifi_config["wifi_ssid"], wifi_config["wifi_pass"])
            print("Status: ", station.status())
            print("isConnected: ", station.isconnected())
            while(station.status() == 1001):
                print("Tentando conectar...")
                time.sleep(1)

            if (station.isconnected()):
                print('Conectado em: ', station.ifconfig())
                return True
            else:
                return False