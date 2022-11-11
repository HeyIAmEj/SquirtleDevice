import uasyncio
from Utils import *
import time

teste = 0

async def ligarBomba():
    global teste
    if (teste == 5):
        print("Ligando a bomba por 15 segundos")
        await uasyncio.sleep_ms(15000)
        print("Saiu")

async def payload_send():
    global teste
    print('Verificando sensor - '+ str(teste))
    teste += 1
    await uasyncio.sleep_ms(1000)

async def main():
    while True:
        uasyncio.create_task(ligarBomba())
        uasyncio.create_task(payload_send())
        await uasyncio.sleep_ms(5000)

uasyncio.run(main())


