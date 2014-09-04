from ardu_py import *
Serial.begin(9600)
debug_print("Ready")
Serial.write("d")
debug_print(Serial.read())
