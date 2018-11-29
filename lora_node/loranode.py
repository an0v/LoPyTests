from machine import Pin
import machine
import binascii

version = 'LoRa node 0.1'

class nodeconfig:
	'''
	Lora-node config class
	'''
	lora_Enabled_port = 'G9'
	def __init__(self):
		self.id = binascii.hexlify(machine.unique_id()).decode('utf-8')

		lora_en_pin = Pin(self.lora_Enabled_port, mode=Pin.IN, pull=Pin.PULL_UP)
		self.lora_enabled = (lora_en_pin.value() == 0)
