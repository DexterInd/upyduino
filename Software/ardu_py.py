import pyb
import ser
import i2c
#Pin Modes
#Ask if this is fine or should be something else??
INPUT=0
INPUT_PULLUP=1
OUTPUT=2

#Debug port initialization
debug = pyb.UART(4, 115200) 
#Serial port initialization
Serial=ser.serial()

Wire=i2c.wire()

HIGH=1
LOW=0

#Pin Definitions
pins={	"RX":pyb.Pin.cpu.C7,	"D0":pyb.Pin.cpu.C7,	0:pyb.Pin.cpu.C7,
		"TX":pyb.Pin.cpu.C6,	"D1":pyb.Pin.cpu.C6,	1:pyb.Pin.cpu.C6,
		"D2":pyb.Pin.cpu.A2,	2:pyb.Pin.cpu.A2,
		"D3":pyb.Pin.cpu.A14,	3:pyb.Pin.cpu.A14,
		"D4":pyb.Pin.cpu.A15,	4:pyb.Pin.cpu.A15,
		"D5":pyb.Pin.cpu.B3,	5:pyb.Pin.cpu.B3,
		"D6":pyb.Pin.cpu.B4,	6:pyb.Pin.cpu.B4,
		"D7":pyb.Pin.cpu.C0,	7:pyb.Pin.cpu.C0,
		"D8":pyb.Pin.cpu.B10,	8:pyb.Pin.cpu.B10,
		"D9":pyb.Pin.cpu.B11,	9:pyb.Pin.cpu.B11,
		"D10":pyb.Pin.cpu.B12,	10:pyb.Pin.cpu.B12,
		"D11":pyb.Pin.cpu.B15,	11:pyb.Pin.cpu.B15,
		"D12":pyb.Pin.cpu.B14,	12:pyb.Pin.cpu.B14,
		"D13":pyb.Pin.cpu.B13,	13:pyb.Pin.cpu.B13,
		"A0":pyb.Pin.cpu.A7,	14:pyb.Pin.cpu.A7,
		"A1":pyb.Pin.cpu.A6,	15:pyb.Pin.cpu.A6,
		"A2":pyb.Pin.cpu.A3,	16:pyb.Pin.cpu.A3,
		"A3":pyb.Pin.cpu.A2,	17:pyb.Pin.cpu.A2,
		"A4":pyb.Pin.cpu.C3,	18:pyb.Pin.cpu.C3,
		"A5":pyb.Pin.cpu.C2,	19:pyb.Pin.cpu.C2,
		"SDA":pyb.Pin.cpu.B7,
		"SCL":pyb.Pin.cpu.B6}
		
#BASIC PIN FUNCTIONS

#pyb.Pin(pins[0],pyb.Pin.IN)
def pinMode(pin_number,mode):
	#??input: pullup or down
	if mode==INPUT:
		pyb.Pin(pins[pin_number],pyb.Pin.IN,pyb.Pin.PULL_NONE)
	elif mode==INPUT_PULLUP:
		pyb.Pin(pins[pin_number],pyb.Pin.IN,pyb.Pin.PULL_UP)
	elif mode==OUTPUT:
		pyb.Pin(pins[pin_number],pyb.Pin.OUT_PP)
		
def digitalWrite(pin_number,state):
	if state==HIGH:
		pins[pin_number].high()
	elif state==LOW:
		pins[pin_number].low()
		
def digitalRead(pin_number):
	return pins[pin_number].value()
	
def analogRead(pin_number):
	return pyb.ADC(pins[pin_number]).read()

#return (pyb.ADC(pins[pin_number]).read())*3.3/4096
def analogReadVoltage(pin_number):
	return (pyb.ADC(pins[pin_number]).read())*5/4096
	
#DEBUG UART FUNCTIONS
def debug_print(msg):
	debug.send(str(msg),timeout=1000)

def debug_println(msg):
	debug.send(str(msg)+"\r\n",timeout=1000)

#Check documentation here: http://stackoverflow.com/questions/10105666/clearing-the-terminal-screen
#Works with putty
def debug_clear():
	debug.send(27,timeout=1000)
	debug.send("[2J",timeout=1000)
	debug.send(27,timeout=1000)
	debug.send("[H",timeout=1000)

#Clear Serial Port when the library is loaded
debug_clear()	

#TIMING FUNCTIONS
def delay(ms):
	pyb.delay(ms)