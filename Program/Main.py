from datetime import datetime
import quandl
import sys
import matplotlib.pyplot as plt
import numpy
import PythonVersion


pythonVData = 0

class StockData:

	def __init__(self):
		print("\tThe Program Has Started...\n")

	def getRecentStockPrice(self, dataSet):
		try:
			print("Processing request...")
			myData = quandl.get(dataSet, returns="numpy")

			print(myData[-1])

			print("Task Complete\n")
		except:
			print("\tThere was an error processing your request. Please try again at a later time.\n")


	def plotHistoricalStockPrice(self, dataSet, startDate, endDate, dataType, iterationType):
		try:
			print("Processing request...")
			myData = quandl.get(dataSet, start_date=startDate, end_date=endDate, collapse=iterationType, returns="numpy")


			print(myData)
			plt.style.use('seaborn-deep')
			#plt.set_title('Historical Stock - {}'.format(dataSet))

			if(dataType.title() == "All"):
				plt.plot(myData['Date'], myData['Low'])
				plt.plot(myData['Date'], myData['Open'])
				plt.plot(myData['Date'], myData['High'])
				plt.plot(myData['Date'], myData['Close'])
				plt.plot(myData['Date'], myData['Adj. Close'])
				plt.legend(['Low', 'Open', 'High', 'Close', 'Adj.Close'])
				plt.ylabel("Price Change")
				plt.xlabel("{} Change".format(iterationType.title()))
			else:
				plt.plot(myData['Date'], myData[dataType])
				plt.legend([''.join(dataType)])
				plt.ylabel("{} - Price Change".format(dataType))
				if(iterationType == "none"):
					plt.xlabel("Complete Change")
				else:
					plt.xlabel("{} Change".format(iterationType.title()))

			plt.show()

			print("Task Complete\n")
		except:
			print("\tThere was an error processing your request. Please try again at a later time.\n")
			print(sys.exc_info()[0])


def main():
	pythonVData = PythonVersion.getPythonVersion()

	program = StockData()
	numpy.set_printoptions(threshold=sys.maxsize)

	while(True):
		print("\t##### MENU #####\n")
		print("\t-- Commands --\n"
			"\tDisplay Stock History - [SH/sh]\n"
			"\tDisplay Stock Data - [SD/sd]\n"
			"\tDebug Test - [U/u]\n"
			"\tQuit - [Q/q]\n")

		if(pythonVData == 3):
			inp = input("Input - ").upper().strip()
		else:
			inp = raw_input("Input - ").upper().strip()

		if(inp == "Q"):
			sys.exit(0)

		if(inp == "SH"):
			if(pythonVData == 3):
				stockID = input("Enter ID [WIKI/...] - ")
				stockStart = input("Enter Start Date [YYYY-MM-DD] - ")
				stockEnd = input("Enter End Date [YYYY-MM-DD] - ")
				stockValue = input("Enter Data Set [Low/High/Close/All/Etc] - ")
				stockIter = input("Enter Iteration Set [Annual/Quarterly/Monthly/Weekly/Daily/None] - ").lower()
			else:
				stockID = raw_input("Enter ID [WIKI/...] - ")
				stockStart = raw_input("Enter Start Date [YYYY-MM-DD] - ")
				stockEnd = raw_input("Enter End Date [YYYY-MM-DD] - ")
				stockValue = raw_input("Enter Data Set [Low/High/Close/All/Etc] - ")
				stockIter = raw_input("Enter Iteration Set [Annual/Quarterly/Monthly/Weekly/Daily/None] - ").lower()
			program.plotHistoricalStockPrice(stockID, stockStart, stockEnd, stockValue, stockIter)

		if(inp == "SD"):
			if(pythonVData == 3):
				stockID = input("Enter ID [WIKI/...] - ")
			else:
				stockID = raw_input("Enter ID [WIKI/...] - ")
			program.getRecentStockPrice(stockID)

		if(inp == "U"):
			print("Debug...")
			print("Debug Complete!")


if __name__ == "__main__":
	quandl.ApiConfig.api_key = "nz915zHdb_vsfnctT6V-"
	main()