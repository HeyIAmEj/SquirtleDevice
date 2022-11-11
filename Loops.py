from Utils import *
from GlobalConst import *
from PayloadSensor import *
import uasyncio

aux = 0
success_times = 0
error_times = 0

async def sta_loop(sta):
    print("entrou no loop")
    while True:
        for x in range(0, 4):
            print("led")
            Utils.successLed().on()
            await uasyncio.sleep_ms(100)
            Utils.successLed().off()
            await uasyncio.sleep_ms(100)
        
        uasyncio.create_task(ligarBomba())
        uasyncio.create_task(payload_send(sta))
        await uasyncio.sleep_ms(5000)

async def ligarBomba():
    global aux
    if (aux == 5 or aux == 20 or aux == 30):
        print("Ligando a bomba por 15 segundos")
        await uasyncio.sleep_ms(15000)
        print("Desligando bomba")

async def payload_send(sta):
    global aux
    global success_times
    global error_times
    
    aux += 1
    print(str(aux)+" - Verificando sensor ASYNC")
    print("chegou no loop sta")
    

    
    if(sta.station.isconnected()):
        error_times = 0
        print("STA Conectado... Success: "+str(success_times))
        #Utils.blinkSuccess()
        
        if(success_times == 2):
            Utils.alertLed().on()
            #get info
            #send payload
            print("instanciando payloadsensor")
            payloadSensor = PayloadSensor()
            print("enviando payload")
            payloadSensor.send()
            
            success_times = 0
            Utils.alertLed().off()
        else:  
            #time.sleep(GlobalConst.WAIT_XSHORT)
            success_times += 1
    else:
        print("Dispositivo não está conectado")
        if(error_times > 2):
#             Utils.blinkError()
            return False
#         time.sleep(GlobalConst.CONNECTION_TRY_AGAIN)



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