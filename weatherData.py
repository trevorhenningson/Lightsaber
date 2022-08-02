from pytz import timezone
import json
from urllib.request import urlopen
import time
import datetime
import jsonManipulation as keyManager

########### Weather:
class Weather:

	apiKey = ""
	location = ""

	def __init__(self, apiKey, location):
		self.apiKey = apiKey
		self.location = location

	def getWeatherURL(self, loc = False, apiKey = False):
		if not loc:
			loc = self.location
		if not apiKey:
			apiKey = self.apiKey

		myURL = 'https://api.openweathermap.org/data/2.5/weather?q=%s&appid=%s&units=imperial' % (loc, apiKey)
		myURL = myURL.strip('\'"')
		return myURL

	def getTemperature(self, loc = False, apiKey = False):
		if not loc:
			loc = self.location
		if not apiKey:
			apiKey = self.apiKey

		myURL = self.getWeatherURL(loc, apiKey)
		response = urlopen(myURL)
		data_json = json.loads(response.read().decode('utf-8'))
		# data_json = json.loads(response.read())
		feelsLike = data_json["main"]["feels_like"]
		return float(feelsLike)

	def printWeather(self, loc = False, apiKey = False):
		if not loc:
			loc = self.location
		if not apiKey:
			apiKey = self.apiKey

		myURL = self.getWeatherURL(loc, apiKey)
		response = urlopen(myURL)
		data_json = json.loads(response.read())
		print("Full:", data_json)
		print("Main:", data_json["main"])
		feelsLike = data_json["main"]["feels_like"]
		print("Feels Like", feelsLike)
		print("")

if __name__ == "__main__":
	key = keyManager.grabKey("Weather")
	weatherLocation = "Philadelphia,PA,USA"

	weatherManager = Weather(key, weatherLocation)

	print(weatherManager.location)
	print(weatherManager.getWeatherURL())
	print(weatherManager.getTemperature())
	weatherManager.printWeather()







