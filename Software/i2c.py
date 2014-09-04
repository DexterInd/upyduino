from pyb import I2C

class wire:
	def begin(self):
		self.i2c = I2C(1, I2C.MASTER) 
		
	def detect(self):
		return self.i2c.scan() 
		
	def recv(self,address,numOfBytes):
		return self.i2c.recv(numOfBytes,address)
		
	def send(self,address,data):
		self.i2c.send(data,address)
