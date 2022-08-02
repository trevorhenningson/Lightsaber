OUT = "out"
IN = "in"
BCM = "IDK"

def setwarnings(setValue):
	print("Warnings set to ", setValue)

def setmode(setValue):
	print("BCM set to", BCM)

def setup(pinNumber, val):
	print("pin %i set to %s" % (pinNumber, val))

def output(port, value):
	print("port %i set to %s" %(port, value))

def input(port):
	return False