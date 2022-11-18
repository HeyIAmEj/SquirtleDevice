# Imports
import esp, gc
gc.collect
from Utils import *
from Loops import *
from StationMode import *
from AccessPointMode import *
from GlobalConst import *
import uasyncio

print("entrou")

# Variaveis e Constantes
running_mode = ""
success_led = Utils.successLed()
error_led = Utils.errorLed()
isStaOn = False
isApOn = False
status_sta = "ok"
status_ap = "ok"

# Starters
Utils.turnOffLeds()
Utils.pump1().off()
Utils.pump2().off()

time.sleep(3)

# Wifi mode
if(Utils.modeButton().value() == 1):
    running_mode = "ap"
else:
    running_mode = "sta"

#Wifi setup
if(running_mode == "sta"):
    print("Iniciando modo STA")
    sta = StationMode()
    try:
        
        sta.station.disconnect()
    except Exception as e:
        print("Erro na inicalização STA: "+e)
        pass
    isStaOn = sta.start()
else:
    try:
        print("Iniciando modo AP")
        ap = AccessPointMode()
        isApOn = True
    except Exception as e:
        print("Erro na inicalização AP: "+e)


# Loop caller
if (isStaOn and running_mode == "sta"):
    print("Mode STA")
    #status_sta = sta_loop(sta)
    status_sta = uasyncio.run(sta_loop(sta))

elif(isApOn and running_mode == "ap"):
    print("Modo AP")
    status_ap = ap_loop(ap)
else:
    print("blink error")
    Utils.blinkAlert()
    Utils.blinkError()
    Utils.blinkAlert()
    Utils.blinkError()
    print("ap mode pois não tem configuração")
    ap = AccessPointMode()
    status_ap = ap_loop(ap)
    
    
if(status_sta == False or status_ap == False):
    #RESTART DEVICE
    print("REINICIAR DISPOSITIVO")
    Utils.alertLed().on()
    Utils.errorLed().on()
    
    
    