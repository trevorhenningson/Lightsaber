import finnhub
from pytz import timezone
import time
import datetime
import jsonManipulation as jsonHelper

class Stocks:
	def __init__(self, apiKey, portfolioFile):
		self.initializeClient(apiKey)
		self.contents = jsonHelper.readStockData()

	def initializeClient(self, apiKey):
		self.finnhub_client = finnhub.Client(api_key=apiKey)

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

	def updatePortfolio(self):

		success = True

		pastHoldings = 0
		currentHoldings = 0

		for stock in self.contents:

			numShares = self.contents[stock]

			try:
				stockInfo = self.finnhub_client.quote(stock)
				previousClose = stockInfo["pc"]
				currentPrice = stockInfo["c"]

				print("%s: %.2f" % (stock, currentPrice * numShares))

				pastHoldings += previousClose * numShares
				currentHoldings += currentPrice * numShares
			except:
				print("Failure to load stock: %s" % stock)
				success = False
		return pastHoldings, currentHoldings, success

	def dayOverDay(self):
		pastHoldings, currentHoldings, success = self.updatePortfolio()
		return currentHoldings - pastHoldings

	def delayTime(self):
		return max(5, len(self.contents) + 1)

if __name__ == "__main__":
	key = jsonHelper.grabKey("Stocks")
	portfolioFile = "stocks.json"

	stockManager = Stocks(key, portfolioFile)
	print(stockManager.updatePortfolio())
	print(stockManager.dayOverDay())
	print(stockManager.delayTime())
