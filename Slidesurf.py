import sys, SendKeys
from bluetooth import *

UUID = "00001101-0000-1000-8000-00805F9B34FB"

class slidesurf:
	def main (self):
		print "searching for devices"
		self.initBlue()
		try:
			while True:
				data = self.client_sock.recv(1024)
				if(data in {"Forward", "Backwards", "B"}):
					if len(data) == 0: break
					print data
					self.parseInput(data)
		except IOError:
			print "error"
			pass	
	    	print "disconnected"
	    	self.client_sock.close()
	    	self.server_sock.close()
	    	print("all done")


	def parseInput(self, input):
		if input == "Forward":
			SendKeys.SendKeys("{RIGHT}")
		if input == "Backwards":
			SendKeys.SendKeys("{LEFT}")
		if input == "B":
			SendKeys.SendKeys("B")

	def initBlue(self):
		self.server_sock = BluetoothSocket( RFCOMM )
		self.server_sock.bind(("", PORT_ANY))
		self.server_sock.listen(1)

		self.port = self.server_sock.getsockname()[1]

		advertise_service( self.server_sock, "SampleServer",
						   service_id = UUID,
						   service_classes = [ UUID, SERIAL_PORT_CLASS],
		#				   protocols = [OBEX_UUID]
							)
		print "waiting for connection on RFCOMM channel %d" % self.port
		self.client_sock, self.client_info = self.server_sock.accept()
		print "Accepted Connection from" , self.client_info
		return True

if __name__ == '__main__':
	ss = slidesurf()
	ss.main()