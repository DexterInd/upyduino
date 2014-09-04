from ardu_py import *
import pwm

py3 = pwm.PWM(pins[4])
for i in range (255):
	py3.duty(i)  
	debug_println(i)
	delay(10)