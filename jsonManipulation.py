## Json Manipulation

import json
import os.path as path

testStockData = {
	"AAPL" : 50.0,
	"ACHR" : 100.0,
	"FSELX" : 80.008,
	"FXAIX" : 10.461,
	"JOBY" : 300.0,
	"MSFT" : 15.0,
	"NWL" : 160.0,
	"RIDE" : 3500.0, 
	"RIVN" : 200.0,
	"SLB" : 350.0, 
}

def grabKey(keyName, fileName = "jsonKeys.json"):

	assert path.exists(fileName), "Key File Does Not Exist"

	with open(fileName) as json_file:
		data = json.load(json_file)
		try: 
			return data[keyName]
		except:
			return False

def getKeyDict(fileName = "jsonKeys.json"):
	assert path.exists(fileName), "Key File Does Not Exist"
	
	with open(fileName) as json_file:
		data = json.load(json_file)
		return data

## Helper function to create a json file from stock data
def createStockFile(stockData = testStockData, fileName = "stocks.json"):
	stockDump = json.dumps(stockData)

	f = open(fileName,'w')
	f.write(stockDump)
	f.close()	

def readStockData(fileName = "stocks.json"):
	assert path.exists(fileName), "Key File Does Not Exist"

	with open(fileName) as json_file:
		data = json.load(json_file)
		return data 

## Helper function to simplify inputting API keys by hand...
def keyInput():
	keyName = input("Type the key name: ")
	keyValue = input("Type the key value: ")

	return (keyName, keyValue)	

def yesNoPrompt(prompt):
	unsatisfied = False

	while not unsatisfied:
		response = input(prompt + ", (y/n): ")

		if response.lower() == "y":
			return True
		if response.lower() == "n":
			return False

def writeKeyFile(fileName):

	keyDict = {}

	prompt1 = "Would you like to add a key?"
	prompt2 = "Would you like to add another key?"

	addKey = yesNoPrompt(prompt1)
	while addKey:
		keyName, keyValue = keyInput()

		keyDict[keyName] = keyValue

		if addKey:
			addKey = yesNoPrompt(prompt2)

	jsonKeys = json.dumps(keyDict)

	f = open(fileName,'w')
	f.write(jsonKeys)
	f.close()



if __name__ == "__main__":
	response = yesNoPrompt("Would you like to create an API Key File?")

	if response:
		fileName = input("What would you like the file name to be? ")

		writeKeyFile(fileName)

	myStockData = {
		"AAPL" : 50.0,
		"ACHR" : 100.0,
		"FSELX" : 80.008,
		"FXAIX" : 10.461,
		"JOBY" : 300.0,
		"MSFT" : 15.0,
		"NWL" : 160.0,
		"RIDE" : 3500.0, 
		"RIVN" : 200.0,
		"SLB" : 350.0, 
	}






