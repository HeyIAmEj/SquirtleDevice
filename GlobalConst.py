from Utils import *

class GlobalConst:
    config = Utils.get_sensor_config()
    
    SETUP_DEVICE_ENDPOINT = "POST /setup_device"
    SETUP_SENSOR_ENDPOINT = "POST /setup_sensor"
    SETUP_RESTART_ENDPOINT = "POST /restart"
    
    GET_SENSOR_INFO_TIME = 60
    CONNECTION_TRY_AGAIN = 5
    WAIT_XSHORT = 5
    WAIT_SHORT = 10
    
    SENSOR1 = 34
    SENSOR1_MAX_POINT = config["sensor1"]["mp"]
    SENSOR1_PUMP_PERCENT = config["sensor1"]["pp"]
    SENSOR1_PUMP_TIME = config["sensor1"]["pt"]
    
    SENSOR2 = 35
    SENSOR2_MAX_POINT = config["sensor2"]["mp"]
    SENSOR2_PUMP_PERCENT = config["sensor2"]["pp"]
    SENSOR2_PUMP_TIME = config["sensor2"]["pt"]

    SENSOR3 = 0
    SENSOR3_MAX_POINT = config["sensor3"]["mp"]
    SENSOR3_PUMP_PERCENT = config["sensor3"]["pp"]
    SENSOR3_PUMP_TIME = config["sensor3"]["pt"]

    SENSOR4 = 0
    SENSOR4_MAX_POINT = config["sensor4"]["mp"]
    SENSOR4_PUMP_PERCENT = config["sensor4"]["pp"]
    SENSOR4_PUMP_TIME = config["sensor4"]["pt"]

    SENSOR5 = 0
    SENSOR5_MAX_POINT = config["sensor5"]["mp"]
    SENSOR5_PUMP_PERCENT = config["sensor5"]["pp"]
    SENSOR5_PUMP_TIME = config["sensor5"]["pt"]

    