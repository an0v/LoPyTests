from network import LoRa
import socket
import machine
import time
import pycom
import paddr

# initialize LoRa in LORA mode
# more params can also be given, like frequency, tx power and spreading factor
client_name = 'client-%d'%(paddr.peer_id,)

print('lopy: %s started' %(client_name,))
while True:
    pycom.rgbled(0x007f00) # green
    # wait a random amount of time
    time.sleep(1000)
    pycom.rgbled(0x7f0000) # red
    time.sleep(1000)
