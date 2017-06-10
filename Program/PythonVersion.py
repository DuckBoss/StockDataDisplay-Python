import platform
from datetime import datetime
from time import strftime

def getPythonVersion():
	pythonVersion = int(platform.python_version()[0])
	if(pythonVersion > 2):
		print("\tCurrently running Python 3")
	else:
		print("\tCurrently running Python 2")
	return pythonVersion

if __name__ == "__main__":
	print(datetime.today().strftime("%Y-%m-%d"))