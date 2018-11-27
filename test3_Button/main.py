import machine
import time
import pycom
import paddr
from machine import Pin

# initialize GP16 in gpio mode (alt=0) and make it an output
led = Pin('G16',mode=Pin.OUT)

# initialize GP17 in gpio mode and make it an input with the
# pull-up enabled
button = Pin('G17', mode=Pin.IN, pull=Pin.PULL_UP)
def callback(p):
    print('pin change', p)
    led.toggle()

button.callback(trigger= Pin.IRQ_FALLING, handler=callback)

pycom.heartbeat(False)
print('stating test 1.1')
print(os.uname())
while True:
    # send some data
    print('toggle led')
    led.toggle()
    print('diod: green')
    pycom.rgbled(0x007f00) # green
    time.sleep(2)
    print('diod: red')
    pycom.rgbled(0x7f0000) # red
    time.sleep(2)
    print('diod: blue')
    pycom.rgbled(0x00007f) # blue
    time.sleep(2)
