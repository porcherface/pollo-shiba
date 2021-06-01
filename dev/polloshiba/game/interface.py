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

class Interface:
	def __init__(self):
		print("interface init")
		ports = []

		# for now i hardcoded the devices
		# [TO-DO] better connection handling
		#ports.append("/dev/ttyUSB1")
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
		print("sending "+msg+" to station "+str(station_id))
		self.iflist[station_id - 1].write( bytes(msg,'ascii') )

	# a blocking function that awaits an acknowledged message
	# from station marked as stationid
	def waitack(self, station_id):
		while True:
			try:
				data_str = self.iflist[station_id-1].read(self.iflist[station_id-1].inWaiting()).decode('ascii') #read the bytes and convert from binary array to ASCII
				if data_str != "" and data_str != " ":
				    if "KO" in data_str:
				        return 0
				    if "OK" in data_str:
				        return 0

			except:
				pass
		