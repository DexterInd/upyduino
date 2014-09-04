from ardu_py import *
Serial.begin(9600)
debug_print("Ready")
while True:
	if (Serial.available()):
		debug_print(Serial.read())