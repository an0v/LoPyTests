from network import LoRa
import socket
import machine
import time
import pycom
import paddr

# initialize LoRa in LORA mode
# more params can also be given, like frequency, tx power and spreading factor
client_name = 'client-%d'%(paddr.peer_id,)

print('peer-NW: %s started' %(client_name,))
lora = LoRa(mode=LoRa.LORA)

# create a raw LoRa socket
s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
pycom.heartbeat(False)
isent_msg = 0
ircvd_msg = 0
while True:
    # send some data
    pycom.rgbled(0x007f00) # green
    s.setblocking(True)
    s.send('%s:sent=%d rcvd=%d'%(client_name,isent_msg,ircvd_msg))
    isent_msg = isent_msg + 1

    # get any data received...
    s.setblocking(False)
    data = s.recv(64)
    if (len(data)>0):
        ircvd_msg = ircvd_msg + 1
        pycom.rgbled(0x7f0000) # red
        print('rcvd[%d]:%s'%(len(data), data))

    # wait a random amount of time
    time.sleep(machine.rng() & 0x0F)
