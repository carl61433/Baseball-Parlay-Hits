# Import the xlrd module
import xlrd
import os
import datetime

# Set CWD to the Players folder with the stats
os.chdir('Players/')
# Import all file names in the Workbooks dir
allFiles = [f for f in os.listdir('.') if os.path.isfile(f)] #Only get files, not folders
#print(allFiles)
dateDictionary = {} #Dictionary to track hits per day
# Open the Workbooks
player1 = xlrd.open_workbook(allFiles[0])
player2 = xlrd.open_workbook(allFiles[1])
stats1 = player1.sheet_by_index(0) #Open the worksheet
stats2 = player2.sheet_by_index(0) #Open the worksheet

def populateDict():
	seasonDay = datetime.date(2023, 3, 30) #Current day of the season
	seasonEnd = datetime.date(2023, 9, 28) #Last day of the season
	while seasonDay <= seasonEnd:
		playerIteration(seasonDay) #Pass the current date to
		#player iteration for checking hits, if there was a game
		seasonDay += datetime.timedelta(days=1) #Next day
	print(dateDictionary)

def playerIteration(date):
	date = date.strftime("%b %-d") #Modifies the date to XXX ## format used in the data
	dateDictionary.update({date:['','']}) #Add the key to the dictionary,
		#with a blank list as the value
	row = 1 #Skip the header, row 0
	while row < 163: #Iterate the rows and columns
		if date == stats1.cell_value(row, 3): #If the current season day is in this row,
			#set the value of the date key to the number of hits
			if stats1.cell_value(row, 12) > 0:
				dateDictionary[date][0] = "yes"
			else:
				dateDictionary[date][0] = "no"
			break
		else:
			dateDictionary[date][0] = "NG"
		row = row + 1
	row = 1 #Reset row for second loop. Skip the header, row 0
	while row < 163:
		if date == stats2.cell_value(row, 3): #If the current season day is in this row,
			#set the value of the date key to the number of hits
			if stats2.cell_value(row, 12) > 0:
				dateDictionary[date][1] = "yes"
			else:
				dateDictionary[date][1] = "no"
			break
		else:
			dateDictionary[date][1] = "NG"
		row = row + 1

def playerHadHit():
	print("")
	#stuff

if __name__=="__main__":
	#playerIteration(allFiles)
	populateDict()
	# Eventually need to compare all six players using the matching date from each dict