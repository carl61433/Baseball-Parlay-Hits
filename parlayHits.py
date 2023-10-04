# Import the xlrd module
import xlrd
import os
import datetime

# Set CWD to the Players folder with the stats
os.chdir('Players/')
# Import all file names in the Workbooks dir
allFiles = os.listdir()
playerHits = {} # Dictionary to store all players and stats
print(allFiles)

def populateDict(allFiles, playerHits):
	# Open the Workbook
	for name in range(len(allFiles)):
		player = xlrd.open_workbook(allFiles[name])

		# Open the worksheet
		stats = player.sheet_by_index(0)

		# Define the dictionary
		datesAndHits = {}

		# Iterate the rows and columns
		for row in range(stats.nrows): # Need to check for proper date format, and remove headers
			if row == 0: # Used to skip the first row of headers
				row = row + 1
			datesAndHits[stats.cell_value(row, 3)] = stats.cell_value(row, 12)
		playerHits[allFiles[name]] = datesAndHits
		#print(datesAndHits)
	#print(playerHits.items())
	# Call next function with playerHits
	#pullSameDate(playerHits, allFiles)

def pullSameDate(playerHits, allFiles):
	# Can use datetime module to iterate through every day of the season
		# which will just have to be set for whichever season
		# Or maybe one day, prompt for the season and players, fetch the start and end dates,
		# then do magic
	currentDate = [] # Variable for storing current date of iteration
	valueLength = [] # Variable for storing the length of each stat dictionary
	key = 1
	#compareDict = {} # Use this dictionary to store each date as a key, and a list of hits on
		# that date as the value?
	for key in range(len(allFiles)): # Not necessary??
		valueLength = len(playerHits[key].keys()[key]) 
	print(valueLength)

if __name__=="__main__":
	populateDict(allFiles, playerHits)

# Eventually need to compare all six players using the matching date from each dict