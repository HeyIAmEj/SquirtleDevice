from Utils import *
from GlobalConst import *
from PayloadSensor import *

def sta_loop(sta):
    print("chegou no loop sta")
    
    success_times = 0
    error_times = 0
    while True:
        if(sta.station.isconnected()):
            error_times = 0
            print("STA Conectado...")
            Utils.blinkSuccess()
            
            if(success_times == 3):
                #get info
                #send payload
                print("instanciando payloadsensor")
                payloadSensor = PayloadSensor()
                print("enviando payload")
                payloadSensor.send()

                Utils.alertLed().on()
                time.sleep(GlobalConst.WAIT_SHORT)
                Utils.alertLed().off()
                success_times = 0
            else:  
                #time.sleep(GlobalConst.WAIT_XSHORT)
                success_times += 1
        else:
            print("Dispositivo não está conectado")
            if(error_times > 2):
                Utils.blinkError()
                return False
            time.sleep(GlobalConst.CONNECTION_TRY_AGAIN)

def ap_loop(apmode):
    status_ap = apmode.start()
    print(apmode.ap.ifconfig())
    if(status_ap == True):
        while True:
            Utils.alertLed().on()
            print("Servidor Rodando")
            status_ap = apmode.server()
            if(status_ap == True):
                Utils.blinkSuccess()
            elif(status_ap  == "restart"):
                Utils.blinkSuccess()
                print("Pedido de restart")
                break
            else:
                Utils.blinkError()
                print("Exceção no server()")
                break
    return False