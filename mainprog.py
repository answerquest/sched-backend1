# mainprog.py
import os

root = os.path.dirname(__file__) # needed for tornado
inputFolder = os.path.join(root,'input')

output1 = os.path.join(root,'output1')
output2 = os.path.join(root,'output2')

os.makedirs(output1, exist_ok=True)
os.makedirs(output2, exist_ok=True)


def computeThis(configD):
	print("Do your computation here")

	full_filename = os.path.join(inputFolder,configD['attachment'])

	logs = []
	logs.append("One log line")

	logs.append("Another log line")

	returnD = { 'message': 'completed', 'logs':logs }

	return returnD
