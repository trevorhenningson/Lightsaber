# Standard Libraries:
import time
import datetime
from pytz import timezone

## GPIO Manipulation
# import RPi.GPIO as GPIO
import testGPIO as GPIO
import piControl as pi

# API Usage:
from weatherData import Weather
from stockData import Stocks

# Data manipulation:
import jsonManipulation as keyManager


############ Helpers:

def confirmValue(val, errorMsg):
	if not val:
		print(errorMsg)


## Pin Info:
def setPin(value):
	if value > 0:
		onlyGreen()
	else: 
		onlyRed()

def setupGPIO():
	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(redGPIO, GPIO.OUT)
	GPIO.setup(greenGPIO, GPIO.OUT)
	GPIO.setup(blueGPIO, GPIO.OUT)

	GPIO.setup(button1GPIO, GPIO.IN) 
	GPIO.setup(button2GPIO, GPIO.IN) 

## Time Settings:
def officeTime(tString):
	hours, minutes, seconds = tString.split(":")

	startingTime = 8
	endingTime = 16
	
	hours = int(hours)
	minutes = int(minutes)

	if hours > endingTime: 
		return False
	elif hours < 8:
		return False
	elif hours < endingTime:
		return True
	return minutes < 30

	return False

def test():
	print("Running a test")
	testTime = 0

	while testTime < 60:
		if testTime % 2 == 0:
			onlyBlue()
			print("blue")
		elif testTime % 3 == 0:
			onlyRed()
			print("red")
		else:
			onlyGreen()
			print("Green")
		testTime += 1
		time.sleep(1)


def updateState(currentState):
	# red, green, blue, stocks, weather, off

	if currentState == 5:
		currentState = 1
	else:
		currentState += 1

	pi.stateChange(currentState)
	return currentState

def onlyRed():
	pi.onlyRed()

def onlyGreen():
	pi.onlyGreen()

def onlyBlue():
	pi.onlyBlue()

def disableLights():
	pi.disableLights()

def stocks():
	dayChange, error = stockManager.dayOverDay()

	if error:
		onlyBlue()
	if dayChange > 0:
		onlyGreen()
	else:
		onlyRed()

	return stockManager.delayTime()

def getMonthRange():
	currentMonth = datetime.datetime.now().month
	

def weather():
	currentTemp = weatherManager.getTemperature()

	datem = datetime.datetime.strptime(date, "%Y-%m-%d %H:%M:%S")

def switch(lightsaberSetting):
	switcher = {
	    1: onlyRed,
	    2: onlyGreen,
	    3: onlyBlue,
	    4: stocks,
	    5: weather,
	    6: disableLights
		}
	
	return switcher.get(lightsaberSetting, disableLights)()

if __name__ == "__main__":

	print("Hello")

	# GPIO Numbers...
	blueGPIO = 26
	greenGPIO = 19
	redGPIO = 13
	button1GPIO = 9
	button2GPIO = 10

	button1State = True
	button2State = True

	# GPIO Setup
	setupGPIO()

	stockManager = Stocks(keyManager.grabKey("Stocks"), "stocks.json")
	weatherManager = Weather(keyManager.grabKey("Weather"), "Moorestown,NJ,USA")

	timeoutTime = datetime.datetime.now(timezone('EST'))
	currentState = 4

	# constant loop
	while True:

		if pi.getInput(button1GPIO):
			if not button1State:
				button1State = True
				print("Button 1 has been Pressed!")
				currentState = updateState(currentState)
				timeoutTime = datetime.datetime.now(timezone('EST'))
		else:
			button1State = False

		if pi.getInput(button2GPIO):
			if not button2State:
				button2State = True
				ip = pi.getIP()
				pi.flashIP(ip)
		else:
			button2State = False

		currentTime = datetime.datetime.now(timezone('EST'))
		timeString = (currentTime.strftime("%X"))

		if currentTime > timeoutTime:
			
			timeOff = switch(currentState)
			if timeOff:
				timeoutTime = currentTime + timeOff

