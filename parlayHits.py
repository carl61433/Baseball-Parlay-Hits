# Import the xlrd module
import xlrd
import os

# Set CWD to the Players folder with the stats
os.chdir('Players/')
# Import all file names in the Workbooks dir
allFiles = os.listdir()
print(allFiles)

#def populateDict(allFiles):
# Open the Workbook
for a in range(len(allFiles)):
	player = xlrd.open_workbook(allFiles[a])

	# Open the worksheet
	stats = player.sheet_by_index(0)

	# Define the dictionary
	datesAndHits = {}

	# Iterate the rows and columns
	for i in range(stats.nrows): # Need to check for proper date format, and remove headers
		for j in range(stats.ncols):
			if j == 12: #add date and corresponding hit count to dict
				if i == 0: # Used to skip the first row of headers
					i = i + 1
				datesAndHits[stats.cell_value(i, 3)] = stats.cell_value(i, j)
	print(datesAndHits)


# Eventually need to compare all six players using the matching date from each dict


# Open first workbook
# Add info to first dict
# Open second workbook

