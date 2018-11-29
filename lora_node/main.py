import machine
import time
import pycom
import loranode
from machine import Pin

pycom.heartbeat(False)
print(os.uname())

# initialize GP16 in gpio mode (alt=0) and make it an output
led = Pin('G16',mode=Pin.OUT)

# initialize GP17 in gpio mode and make it an input with the
# pull-up enabled
button = Pin('G17', mode=Pin.IN, pull=Pin.PULL_UP)
counter = 0
def callback(p):
    global counter
    print('pin change. counter', counter)
    led.toggle()
    counter = counter + 1

button.callback(trigger= Pin.IRQ_FALLING, handler=callback)

cfg = loranode.nodeconfig()
print(loranode.version)
print('cfg:node_id: ', cfg.id)
print('cfg:LoRa_enabled: ', cfg.lora_enabled)

#while True:
for cycles in range(3): # stop after 5 cycles
    # send some data
    print('diod: green ',cycles)
    pycom.rgbled(0x007f00) # green
    time.sleep(2)
    print('diod: red ',cycles)
    pycom.rgbled(0x7f0000) # red
    time.sleep(2)
    print('diod: blue ',cycles)
    pycom.rgbled(0x00007f) # blue
    time.sleep(2)
