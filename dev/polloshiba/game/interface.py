######################################################################
# file: interface.py
# version: 1.0.0
# author: porcherface
# descr: pollo-station and pollo spotlight connection interface
######################################################################
		
# SERIAL PORTS SETTINGS

import serial

class Interface:
	def __init__(cls):
		print("interface init")
		ports = []
		#ports.append("/dev/ttyUSB1")
		#ports.append("/dev/ttyUSB2")
		#ports.append("/dev/ttyUSB3")
		#ports.append("/dev/ttyUSB4")
		baudrate = 115200 
		cls.iflist = []
		for port in ports:		
			cls.iflist.append(serial.Serial(port, baudrate) )


	def testConnection(self):
		pass

	def send(self, msg, station_id):
		print("sending "+msg+" to station "+str(station_id))

	def waitack(self, station_id):
		pass