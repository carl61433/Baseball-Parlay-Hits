#Compares players to see how many times in a season they each got a hit on the same day.
import xlrd #Import the xlrd module
import os
import datetime
#from players import player #My player class

# Set CWD to the Players folder with the stats
os.chdir('Players/')
# Import all file names in the Workbooks dir
allFiles = [f for f in os.listdir('.') if os.path.isfile(f)] #Only get files, not folders
playerDictionary = {} #Dictionary to associate player names with their stats
dayOfWeekCounter = {"Monday":0,"Tuesday":0,"Wednesday":0,"Thursday":0,"Friday":0,"Saturday":0,"Sunday":0}
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

def playerInit(): #Create the dictionary of players, with filename as key and the worksheet as the value
	for i in allFiles:
		workbook = xlrd.open_workbook(i)
		stats = workbook.sheet_by_index(0)
		playerDictionary.update({i:stats})
	populateDict()

def populateDict():
	dateDictionary = {} #Dictionary to track hits per day
	seasonDay = datetime.date(2023, 3, 30) #Current day of the season
	seasonEnd = datetime.date(2023, 9, 28) #Last day of the season
	while seasonDay <= seasonEnd:
		playerIteration(seasonDay, dateDictionary) #Pass the current date to
		#player iteration for checking hits, if there was a game
		seasonDay += datetime.timedelta(days=1) #Next day
	numberOfDays(dateDictionary)

def playerIteration(seasonDay, dateDictionary):
	date = seasonDay.strftime("%b %-d") #Modifies the date to 'XXX ##' format used in the data
	dateDictionary.update({seasonDay:[]}) #Add the date as a  key to the dictionary,
		#with a blank list as the value
	for player in playerDictionary:
		row = 0
		while row < playerDictionary[player].nrows - 1:
			gameCheckCounter = 0 #Essentially a boolean to check if an entry was made for that date
			if date == playerDictionary[player].cell_value(row, 3): #If the current season day is in this row,
				#set the value of the date key to the number of hits
				if playerDictionary[player].cell_value(row, 12) > 0:
					dateDictionary[seasonDay].append("yes")

				else:
					dateDictionary[seasonDay].append("no")
				gameCheckCounter = 1
				break
			row += 1
		if gameCheckCounter == 0:
			dateDictionary[seasonDay].append("NG")

def numberOfDays(dateDictionary): #The number of times that this occurred in the season.
	counter = 0
	for i in dateDictionary:
		if len(set(dateDictionary[i])) == 1 and dateDictionary[i][0] == "yes":
			counter = counter + 1
			dayOfWeekCounter[days[i.weekday()]] += 1
	print("These players have hit on the same day " + str(counter) + " times this season.")
	print(dayOfWeekCounter)

if __name__=="__main__":
	playerInit()