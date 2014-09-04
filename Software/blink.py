from ardu_py import *
i=0
pin=3
pinMode(pin,INPUT)
for i in range (100):
	digitalWrite(pin,HIGH)
	debug_print(i)
	delay(500)
	digitalWrite(pin,LOW)
	debug_print(i)
	delay(500)