# Import the xlrd module
import xlrd
import os

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
	print(playerHits.items())
	return(playerHits)
	# Call next function with playerHits
	# pullSameDate(playerHits)

def pullSameDate(playerHits):
	print("")

if __name__=="__main__":
	populateDict(allFiles, playerHits)

# Eventually need to compare all six players using the matching date from each dict