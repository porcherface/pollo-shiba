######################################################################
# file: interface.py
# version: 1.0.0
# author: porcherface
# descr: pollo-station and pollo spotlight connection interface
######################################################################
		
# [TO-DO] a ripoff code for a singleton (da vedere e magari implementare 
# in una versione futura di pollo shiba)
''' we are still reasoning on wheter make a singleton or not
	just in case, i ripoff a singleton class


class Singleton(type):
    def __init__(cls, name, bases, dict):
        super(Singleton, cls).__init__(name, bases, dict)
        cls.instance = None

class GlobalClass(object):
    __metaclass__ = Singleton 
    def __init__():
        print("I am global and whenever attributes are added in one instance, any other instance will be affected as well.")
'''

# a handler class for connectioninterfaces, handles message dispatch and event catcher from
# connection channels. the hardware-software communication logic is heavily hardcoded here.


# for version 1.0.0 -  serial connection arduino-like
import serial
import pygame

TIMEOUT_EVENT_KEY =  pygame.USEREVENT + 1
TRIGGER_EVENT_KEY =  pygame.USEREVENT + 2
BUTTON1_EVENT_KEY =  pygame.USEREVENT + 3
BUTTON2_EVENT_KEY =  pygame.USEREVENT + 4
START_EVENT_KEY = pygame.USEREVENT + 5
WIN_EVENT_KEY = pygame.USEREVENT + 6

TRIGGER_EVENT=pygame.event.Event(TRIGGER_EVENT_KEY)
TIMEOUT_EVENT=pygame.event.Event(TIMEOUT_EVENT_KEY)
BUTTON1_EVENT=pygame.event.Event(BUTTON1_EVENT_KEY)
BUTTON2_EVENT=pygame.event.Event(BUTTON2_EVENT_KEY)
START_EVENT=pygame.event.Event(START_EVENT_KEY)
WIN_EVENT=pygame.event.Event(WIN_EVENT_KEY)

# event key, used also in interface.py (actually hardcoded)
TIMEOUT_EVENT_KEY =  pygame.USEREVENT + 1

class Interface:

	# we better make an explic initializer ?
	def __init__(self):
		self.INITIALIZED = False
		self.TRIGGERED = False
		self.BUTTON_1 = False
		self.BUTTON_2 = False

	def initialize(self):
		print("interface init")
		self.INITIALIZED = True
		ports = []

		# for now i hardcoded the devices
		# [TO-DO] better connection handling
		ports.append("/dev/ttyACM0")
		#ports.append("/dev/ttyUSB2")
		#ports.append("/dev/ttyUSB3")
		#ports.append("/dev/ttyUSB4")

		# connection settings
		baudrate = 115200 
		self.iflist = []
		for port in ports:		
			self.iflist.append(serial.Serial(port, baudrate) )
			# we might wanna add a check isOpen code here

		# or here
		return


	# a null function
	def testConnection(self):
		pass

	# sends msg to station labeled as station_id
	def send(self, msg, station_id):
		if self.INITIALIZED:
			print("sending "+msg+" to station "+str(station_id))
			self.iflist[station_id - 1].write( bytes(msg,'ascii') )

	# a blocking function that awaits an acknowledged message
	# from station marked as stationid
	def waitack(self, station_id):
		while True and self.INITIALIZED:
			try:
				data_str = self.iflist[station_id-1].read(self.iflist[station_id-1].inWaiting()).decode('ascii') #read the bytes and convert from binary array to ASCII
				out_str = ""
				if data_str != "" and data_str != " ":
					if "KO" in data_str:
						out_str = data_str.split("$")[1]
						return out_str
					if "OK" in data_str:
						out_str = data_str.split("$")[1]
						return out_str
			except:
				pass
		
		if not self.INITIALIZED:
			print("interface not inizialized")
			return "[NA]"
	def waitacksmanettino(self, station_id):
		while True and self.INITIALIZED:
			try:
				data_str = self.iflist[station_id-1].read(self.iflist[station_id-1].inWaiting()).decode('ascii') #read the bytes and convert from binary array to ASCII
				if data_str != "" and data_str != " ":
					print("data received: "+data_str)
					if "KO" in data_str:
						print("received KO ack")
						return "[KO]"
					if "L01_HI" in data_str:
						print("received OK ack")
						return "[OK]"
			except:
				pass
		
		if not self.INITIALIZED:
			print("interface not inizialized")
			return "[NA]"

	def readSerialThreaded(self):
		while True and self.INITIALIZED:
			for station in self.iflist:
				try:
					data_str = station.read(station.inWaiting()).decode('ascii') #read the bytes and convert from binary array to ASCII
					if "TRIGGER" in data_str:
						print("TRIGGER DETECTED!")
						self.TRIGGERED = True
						pygame.event.post(TRIGGER_EVENT)
						
					if "B01_DN" in data_str:
						print("button 1 PRESSED")
						self.BUTTON_1 = True
						pygame.event.post(BUTTON1_EVENT)
						

					if "B02_DN" in data_str:
						print("button 2 PRESSED")
						self.BUTTON_2 = True
						pygame.event.post(BUTTON2_EVENT)
					

				except:
					pass
		
		if not self.INITIALIZED:
			print("interface not initialized")


	def trigger_kill(self):

		if self.INITIALIZED:
			for station in self.iflist:
				station.write( bytes("#pollo$TRIGGER@",'ascii') )