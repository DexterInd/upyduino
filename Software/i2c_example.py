from ardu_py import *
Wire.begin()
debug_println(Wire.recv(10,6))
Wire.send(10,"asd")