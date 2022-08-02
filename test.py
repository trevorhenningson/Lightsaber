from urllib.request import urlopen
import json
import socket
import time

def getWeatherURL(location):
	apiKey = 'd7c7d1a63602e124927faee223207567'
	myURL = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=imperial' % (location, apiKey)
	myURL = myURL.strip('\'"')
	return myURL

def printWeather(loc):
	myURL = getWeatherURL(loc)
	response = urlopen(myURL)
	data_json = json.loads(response.read())
	print("Full:", data_json)
	print("Main:", data_json["main"])
	feelsLike = data_json["main"]["feels_like"]
	print("Feels Like", feelsLike)
	print("")

def getMapsURL(locationA, locationB):
	apiKey = "O1s0wwMRDXHLDK5LD6gbTflZVMCDKpmW"
	
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
	

def splitIP(ipAddress):
	split = ipAddress.split(".")
	for splitted in split:
		binary = format(int(splitted), "b")
		for number in binary:
			if number == "1":
				print(1)
			else:
				print(0)
			time.sleep(.5)
		print("...")

if __name__ == "__main__":
	printWeather("Cherry%20Hill,NJ,USA")
	ipAddress = getIP()
	splitIP(ipAddress)