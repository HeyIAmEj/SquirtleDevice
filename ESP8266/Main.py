# Imports
from Utils import *
from Loops import *
from StationMode import *
from AccessPointMode import *
from GlobalConst import *


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



# Wifi mode
running_mode = "sta"

#Wifi setup
if(running_mode == "sta"):
    sta = StationMode()
    sta.station.disconnect()
    isStaOn = sta.start()
else:
    ap = AccessPointMode()
    isApOn = True


# Loop caller
if (isStaOn and running_mode == "sta"):
    print("Mode STA")
    status_sta = sta_loop(sta)

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
    
    
    