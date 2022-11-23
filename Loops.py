from Utils import *
from GlobalConst import *
from PayloadSensor import *
import uasyncio

aux = 0
success_times = 0
error_times = 0

isPumpWaiting = {
            "sensor1":False,
            "sensor2":False,
            "sensor3":False,
            "sensor4":False,
            "sensor5":False
            }

async def sta_loop(sta):
    print("entrou no loop")
    while True:        
        #uasyncio.create_task(ligarBomba())
        uasyncio.create_task(payload_send(sta))
        await uasyncio.sleep_ms(5000)

async def ligarBomba1(pp):
    Utils.pump1().off()
    global isPumpWaiting
    isPumpWaiting["sensor1"] = True
    print("\n\nLigando a bomba 1 por {} segundos\n".format(int(pp)))
    Utils.pump1().on()
    await uasyncio.sleep(pp)
    print("\n\nDesligando bomba 1")
    Utils.pump1().off()
    await uasyncio.sleep(20) #30 segundos de espera
    isPumpWaiting["sensor1"] = False
async def ligarBomba2(pp):
    Utils.pump2().off()
    global isPumpWaiting
    isPumpWaiting["sensor2"] = True
    print("\n\nLigando a bomba 2 por {} segundos\n".format(int(pp)))
    Utils.pump2().on()
    await uasyncio.sleep(pp)
    print("\nDesligando bomba 2")
    Utils.pump2().off()
    await uasyncio.sleep(20) #30 segundos de espera
    isPumpWaiting["sensor2"] = False

async def payload_send(sta):
    global aux
    global success_times
    global error_times
    
    aux += 1    

    if(sta.station.isconnected()):
        print("\nDispositivo conectado.")
        error_times = 0
        Utils.blinkSuccess()
        
        if(success_times == 5):
            Utils.alertLed().on()
            payloadSensor = PayloadSensor()
            print("Enviando payload")
            payloadSensor.send()
            
            success_times = 0
            Utils.alertLed().off()
        else:  
            success_times += 1
            
        # verifica se deve fazer bombeamento automatico
        state = Utils.get_wifi_config()["status"]
        if(state == "Ativado"):
            # pode bombear automaticamente
            #print("Bombeamento automático ativado!")
            sensorinfo = SensorInfo()
            status = sensorinfo.get_activate_pump()
            print(status)
            global isPumpWaiting
            for x in status:
                if x == "sensor1":
                    if(status[x] == True and isPumpWaiting["sensor1"] == False):
                        uasyncio.create_task(ligarBomba1(GlobalConst.SENSOR1_PUMP_TIME))
                    elif (isPumpWaiting["sensor1"] == True):
                        print("Não pode iniciar bomba 1, por causa do tempo de absorção")
                elif(x == "sensor2"):
                    if(status[x] == True and isPumpWaiting["sensor2"] == False):
                        uasyncio.create_task(ligarBomba2(GlobalConst.SENSOR1_PUMP_TIME))
                    elif (isPumpWaiting["sensor2"] == True):
                        print("Não pode iniciar bomba 2, por causa do tempo de absorção")
    else:
        print("Dispositivo não está conectado")
        if(error_times > 2):
            Utils.blinkError()
            return False



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