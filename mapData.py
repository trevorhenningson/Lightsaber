from pytz import timezone
import json
from urllib.request import urlopen
import time
import datetime
import jsonManipulation as keyManager

########### Weather:
class Maps:

	apiKey = ""
	location = ""

	def __init__(self, apiKey, starting, ending):
		self.apiKey = apiKey
		self.starting = starting
		self.ending = ending 

	def getMapRouteURL(self, starting = False, ending = False, apiKey = False):
		if not starting:
			starting = self.starting
		if not ending:
			ending = self.ending
		if not apiKey:
			apiKey = self.apiKey

		myURL = "https://api.tomtom.com/routing/1/calculateRoute/"
		myURL += starting + ":"
		myURL += ending
		myURL += "/json?routeRepresentation=summaryOnly&routeType=fastest&traffic=true&key=%s" % apiKey
		
		return myURL

	def getRoute(self, starting = False, ending = False, apiKey = False):
		if not starting:
			starting = self.starting
		if not ending:
			ending = self.ending
		if not apiKey:
			apiKey = self.apiKey

		myURL = self.getMapRouteURL(starting, ending, apiKey)
		response = urlopen(myURL)

		data_json = json.loads(response.read())
		print("Full:", data_json)
		print("Routes:", data_json["routes"])
		travelTime = data_json["routes"][0]["summary"]["travelTimeInSeconds"]
		trafficDelay = data_json["routes"][0]["summary"]["trafficDelayInSeconds"]
		print("Delay: ", trafficDelay)
		print("Total Time: ", travelTime)
		print("")

	def getDelay()
		myURL = self.getMapRouteURL(starting, ending, apiKey)
		response = urlopen(myURL)

		trafficDelay = data_json["routes"][0]["summary"]["trafficDelayInSeconds"]
		return trafficDelay

	def getTotalTime()
		myURL = self.getMapRouteURL(starting, ending, apiKey)
		response = urlopen(myURL)

		trafficDelay = data_json["routes"][0]["summary"]["travelTimeInSeconds"]
		return trafficDelay


if __name__ == "__main__":
	key = keyManager.grabKey("Maps")

	slbRosharon = "29.369761491768053,-95.44032360371638"
	circleAtHermann = "29.717824428555325,-95.38149686040018"
	westminster = "33.847790796962194,-84.43337746636308"
	ATL = "33.64076407111493,-84.44645867900734"
	oraclePark = "37.77850485799018,-122.38936912400277"
	endor = "37.8288194798984,-122.4861098025627"
	oakland = "37.80470730494777,-122.2713473805796"

	# Texas locations...
	defaultStarting = oakland
	defaultEnding = oraclePark


	mapManager = Maps(key, defaultStarting, defaultEnding)


	print(mapManager.getMapRouteURL())
	mapManager.getRoute()
