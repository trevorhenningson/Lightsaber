# Testing functionality of led beping

import RPi.GPIO as GPIO
import time
import finnhub
import datetime
from pytz import timezone

contents = {
	"AAPL" : 50.0,
	"ACHR" : 100.0,
	"JOBY" : 300.0,
	"MSFT" : 15.0,
	"NWL" : 160.0,
	"RIDE" : 3500.0, 
	"SLB" : 350.0, 
}

def updatePortfolio():
	cash = 	10458.58

	pastHoldings = cash
	currentHoldings = cash

	for stock in contents:

		numShares = contents[stock]

		stockInfo = finnhub_client.quote(stock)
		previousClose = stockInfo["pc"]
		currentPrice = stockInfo["c"]

		pastHoldings += previousClose * numShares
		currentHoldings += currentPrice * numShares

	return pastHoldings, currentHoldings

def setPin(value):
	if value > 0:
		onlyGreen()
	else: 
		onlyRed()

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

def setBlue(on):
	toggleGPIO(bluePin, on)

def setRed(on):
	toggleGPIO(redPin, on)

def setGreen(on):
	toggleGPIO(greenPin, on)

def disableLights():
	setBlue(False)
	setRed(False)
	setGreen(False)

def toggleGPIO(port, on):
	GPIO.output(port, on)

def tradingTime(tString):
	hours, minutes, seconds = tString.split(":")

	hours = int(hours)
	minutes = int(minutes)

	if hours >= 16: 
		return False
	elif hours < 9:
		return False
	elif hours > 10:
		return True
	return minutes > 30

	return True

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



if __name__ == "__main__":

	redPin = 11
	bluePin = 10
	greenPin = 9

	GPIO.setwarnings(False)
	GPIO.setmode(GPIO.BCM)

	GPIO.setup(bluePin, GPIO.OUT)
	GPIO.setup(greenPin, GPIO.OUT)
	GPIO.setup(redPin, GPIO.OUT)

	finnhubKey = keyManager.grabKey("Stocks")

	finnhub_client = finnhub.Client(api_key=finnhubKey)

	onlyBlue()	

	# while True:
	# 	currentTime = datetime.datetime.now(timezone('EST'))
	# 	timeString = (currentTime.strftime("%X"))
		
	# 	print("Timezone is %s" % currentTime.strftime("%Z"))
	# 	print("Current Time Is: %s" % timeString)

	# 	if tradingTime(timeString):
	# 		past, current = updatePortfolio()
	# 		todayDelta = current - past

	# 		print("Past Holdings $%.2f" % past)
	# 		print("Current Holdings $%.2f" % current)
		
	# 		setPin(todayDelta)
	
	# 		time.sleep(100/len(contents))
	# 	elif officeTime(timeString): 
	# 		onlyBlue()
	# 		print("Office Time")
	# 		time.sleep(5)
	# 	else:
	# 		print("All Off")
	# 		disableLights()
	# 		time.sleep(5)


