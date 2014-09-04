from ardu_py import *
i=0
pin=3
pinMode(pin,INPUT)
for i in range (100):
	ip=digitalRead(pin)
	debug_println(ip)
	delay(100)