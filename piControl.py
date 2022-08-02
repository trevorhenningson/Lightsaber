# import RPi.GPIO as GPIO
import testGPIO as GPIO

import time
import datetime
import socket


## Flashing...
def flashGreen(flashTime = .25):
	setGreen(True)
	time.sleep(flashTime)
	disableLights()
	time.sleep(flashTime)

def flashBlue(flashTime = .25):
	setBlue(True)
	time.sleep(flashTime)
	disableLights()
	time.sleep(flashTime)

def flashRed(flashTime = .25):
	setRed(True)
	time.sleep(flashTime)
	disableLights()
	time.sleep(flashTime)

## Solids...
def onlyGreen():
	setGreen(True)
	setRed(False)
	setBlue(False)

def onlyBlue():
	setBlue(True)
	setRed(False)
	setGreen(False)

def onlyRed():
	setRed(True)
	setGreen(False)
	setBlue(False)

## Individuals...
def setBlue(on):
	toggleGPIO(blueGPIO, on)

def setRed(on):
	toggleGPIO(redGPIO, on)

def setGreen(on):
	toggleGPIO(greenGPIO, on)

## Disabling...
def disableLights():
	setBlue(False)
	setRed(False)
	setGreen(False)

## Toggling on/off
def toggleGPIO(port, on):
	GPIO.output(port, on)

## Reading Input...
def getInput(gpioNumber):
	return GPIO.input(gpioNumber)

## Changing state
def stateChange(state):
	print("Current State = %i" % state)

	if state == 1:
		flashRed()
	elif state == 2:
		flashGreen()
	elif state == 3: 
		flashBlue()
	elif state == 4:
		flashRed()
		flashRed()
		flashGreen()
		flashGreen()
	elif state == 5:
		flashBlue()
		flashGreen()
		flashRed()
	elif state == 6:
		flashGreen()
		flashRed()
		flashGreen()
		flashRed()

## Extras...
## IP Manipulation...
def getIP():
	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.settimeout(0)
	try:
		# doesn't even have to be reachable
		s.connect(('10.255.255.255', 1))
		IP = s.getsockname()[0]
	except Exception:
		IP = '127.0.0.1'
	finally:
		s.close()
	return IP
	

def flashIP(ipAddress):
	split = ipAddress.split(".")
	for splitted in split:
		binary = format(int(splitted), "b")
		for number in binary:
			if number == "1":
				flashGreen(flashTime = .4)
			else:
				flashRed(flashTime = .4)
		flashBlue(flashTime = .4)


