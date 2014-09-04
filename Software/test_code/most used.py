# main.py -- put your code here!
from pyb import UART
uart = UART(3, 9600) 
gps= UART(6, 9600) 
data=bytearray(2)
while True:
	if gps.any():
		gps.recv(data, timeout=5000)
		uart.send(data,timeout=1000)
		
from pyb import UART
uart = UART(4, 115200) 
data=bytearray(1)
data[0]=113
uart.send(data,timeout=1000)


a5=pyb.ADC(pyb.Pin.board.C2)
a4=pyb.ADC(pyb.Pin.board.C3)
a3=pyb.ADC(pyb.Pin.board.A2)
a2=pyb.ADC(pyb.Pin.board.A3)
a1=pyb.ADC(pyb.Pin.board.A6)
a0=pyb.ADC(pyb.Pin.board.A7)
while True:
	print (a0.read(),"\t",a1.read(),"\t",a2.read(),"\t",a3.read(),"\t",a4.read(),"\t",a5.read())