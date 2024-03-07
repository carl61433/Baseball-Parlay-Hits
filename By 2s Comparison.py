#Compares each player with one other player, and outputs to CSV in a readable chart.
import xlrd #Import the xlrd module
import os
import datetime
import csv
#from players import player #My player class

# Set CWD to the Players folder with the stats
os.chdir('Players/')
# Import all file names in the Workbooks dir
allFiles = [f for f in os.listdir('.') if os.path.isfile(f)] #Only get files, not folders
playerDictionary = {} #Dictionary to associate player names with their stats
playerDatesAndHits = {} #Dictionary to keep track of player results, using nested dictionaries
playerDaysHit = {}

def playerInit(): #Create the dictionary of players, with filename as key and the worksheet as the value
	for i in allFiles:
		playerName = i[:-4] #Drop the '.xls' part
		workbook = xlrd.open_workbook(i)
		stats = workbook.sheet_by_index(0)
		playerDictionary.update({playerName:stats})
		playerDatesAndHits[playerName] = {}
		playerDaysHit[playerName] = 0
	populateDateDict()

def populateDateDict():
	seasonDay = datetime.date(2023, 3, 30) #Current day of the season
	seasonEnd = datetime.date(2023, 9, 28) #Last day of the season
	while seasonDay <= seasonEnd:
		playerIteration(seasonDay) #Pass the current date to
		#player iteration for checking hits, if there was a game
		seasonDay += datetime.timedelta(days=1) #Next day
	numberOfDays()

def playerIteration(date):
	date = date.strftime("%b %-d") #Modifies the date to XXX ## format used in the data
	for player in playerDictionary:
		dayCounter = 0
		row = 0
		while row < playerDictionary[player].nrows - 1:
			gameCheckCounter = 0 #Essentially a boolean to check if an entry was made for that date
			if date == playerDictionary[player].cell_value(row, 3): #If the current season day is in this row,
				#set the value of the date key to the number of hits
				if playerDictionary[player].cell_value(row, 12) > 0:
					playerDatesAndHits[player].update({date:"yes"})
					dayCounter += 1
				else:
					playerDatesAndHits[player].update({date:"no"})
				gameCheckCounter = 1
				break
			row += 1
		if gameCheckCounter == 0:
			playerDatesAndHits[player].update({date:"NG"})
		playerDaysHit[player] += dayCounter

def numberOfDays(): #The number of times that this occurred in the season.
	playerCompare = {}
	for i in playerDatesAndHits:
		playerCompare.update({i:[]})
		for j in playerDatesAndHits:
			counter = 0
			dayCounter = 0
			if j == i:
				playerCompare[i].append("x")
				continue
			seasonDay = datetime.date(2023, 3, 30) #Current day of the season
			seasonEnd = datetime.date(2023, 9, 28) #Last day of the season
			while seasonDay <= seasonEnd:
				date = seasonDay.strftime("%b %-d")
				if playerDatesAndHits[i][date] == "yes" and playerDatesAndHits[j][date] == "yes":
					counter += 1
				seasonDay += datetime.timedelta(days=1) #Next day
			if j != i:
				playerCompare[i].append(counter)
			for item in range(len(playerCompare[i])):
				if playerCompare[i][item] == "x":
					break
				else:
					playerCompare[i][item] = ''
	os.chdir('..')
	with open('By2s.csv', 'w', newline='') as file:
		playerList = []
		writer = csv.writer(file)
		topRow = ['NAME:']
		topRow += list(playerCompare.keys())
		topRow += ['# Days']
		writer.writerow(topRow)
		for player in playerCompare:
			playerList = []
			playerList.append(player)
			for x in range(len(playerCompare[player])):
				playerList.append(playerCompare[player][x])
			playerList.append(playerDaysHit[player])
			writer.writerow(playerList)

if __name__=="__main__":
	playerInit()