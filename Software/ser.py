from pyb import UART
class serial:
	data=bytearray(1)
	time_out=1000
	def begin(self,baudrate):
		self.uart= UART(6, baudrate)
		
	def read(self):
		self.uart.recv(self.data, timeout=1000)
		return chr(self.data[0])
	
	def available(self):
		return self.uart.any()