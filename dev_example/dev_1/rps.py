""" 
Rock Scissors Paper (RPS) games
This program will use a simple menu to allow the player to play RPS or 
have the game play RPS.  

If the user selects human play, then they are presented with another menu 
to select their RPS choice or stop playing.  If user selects stop playing then they are shown statistics for their game play and return to beginning menu. 

To play RPS the user now needs to provide an email address, which is validated by regex and is used the store the RPS outcome into a txt file in the simple format for 'player@email.com win'.  The game now allows the player to change the current play and display a leader board. 

The leaderboard reads each entry in the games.txt and builds an list that is then used the filter by wins and sorted to show the leaderboard. 

"""
# import random from standar library
import os
import sys
from collections import defaultdict
import random


# Global Player Name
playerName = False

# Global list for tracking games outcomes - 'win', 'loss', 'tie'
games = []

# function to determine the outcomes of a RSP game
# returns str and updates global list for tracking game outcomes

def determineRPS(playerChoice, gameChoice, player):
    result = ''
    outputMessage = ''
    
    if playerChoice == gameChoice:
        result = 'tie'
        outputMessage = 'Tie - either Wins'
    if playerChoice == 'rock':
        if gameChoice == 'scissors':
            outputMessage = 'Rock beats Scissors - Player Wins'
            result = 'win'
        else:
            outputMessage = 'Scissors beats Paper - Game Wins'
            result = 'loss'
    if playerChoice == 'paper':
        if gameChoice == 'rock':
            outputMessage = 'Paper beats Rock - Player Wins'
            result = 'win'
        else:
            outputMessage = 'Scissors cuts Paper - Game Wins'
            result = 'loss'
    if playerChoice == 'scissors':
        if gameChoice == 'paper':
            outputMessage = 'Scissors Cut Paper = Player Wins'
            result = 'win'
        else:
            outputMessage = 'Rock crushes Scissors -  Game Wins'
            result = 'loss'
    #Add result to game.txt

    games.append(result)
    writeToFile(player, result)
    return outputMessage        

#function handle getting user input for main menu, also includes try except error handling
def getUserInput(message):
    try:
        userInput = int(input(message))
    except ValueError:
        print('Enter a numeric value')
    else:
        return userInput

#function takes in selection (intergar) and returns user selection as str or error
#note: will refactor for try except

def determineRPS_str(selection):
    if(selection == 1):
        return('rock')
    elif(selection == 2):
        return('scissors')
    elif(selection == 3):
        return('paper')
    elif(selection == 0):
        return('done')
    else:
        return('error')


def writeToFile(player, result):
    dirname, filename = os.path.split(os.path.abspath(__file__))

    try:
        game_file = open(dirname + '/games.txt', 'a')
        game_file.writelines(player + ' ' + result + "\n")
        game_file.close()
    except IOError:
        print('Error while writing to file')


def readFile():
    #determine dirname of game.txt
    dirname, filename = os.path.split(os.path.abspath(__file__))

    #declare empty list
    games = []
    filepath = dirname + '/games.txt' 

    #open 
    try:
        with open(filepath) as fp:
            game = fp.readline()
            while game:
                game_list = game.rstrip().split(' ')
                games.append(game_list)
                game = fp.readline()
            return games
    except IOError:
                print('error reading file')
                return []
            
    

def leaderBoard():
    #read games.text into memory
    games = readFile()
    if len(games) > 0:
        #filter by str 'win' to get all wins out of games.txt
        win = list(filter(lambda x: x[1] == 'win', games))
    
        #setup data dictonary 
        winLeader = defaultdict(int)

        #for each entry in win count by player
        for player in win:
            winLeader[player[0]] +=1
        
        # Display to User
        print('---------------- Current Leader Board by games WON!!!!  ---------------------\n')    
        print({k: v for k, v in sorted(
            winLeader.items(), key=lambda item: item[1], reverse=True)})

    else:
        print('No data in game file')

# function show game play statistics
def showStats():
    global games
    print('--------------------------------Game Statics here----------------------------------')
    print('Total Games Played for this sesssion' + str(len(games)))
    print('Player won ' + str(games.count('win')))
    games = []

# this function will handle validation of email input and use email as the player name
import re

def validateEmail():
    while(True):
        print('-------------------- Our game uses email for your Player Name ---------------------- ')
        playerName = input('email? --> ')
        if (re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$', playerName)):
            print('email is valid')
            return playerName
        else: 
            print('email is not valid')

# function handles the user playing RPS as many times as they like and once they select 0 to stop they are
# shown game statistics

def userPlays():
    global playerName
    playRPS = True
    if not playerName:
        playerName = validateEmail()
    while(playRPS):
        
        print(
            '----------------------------------- Current Player is ' + playerName + ' -------------------------------')
        playerChoice = determineRPS_str(getUserInput(
            '0: Stop Playing\n1: Rock\n2: Scissors\n3: Paper\nYour Choice > '))
        
        if(playerChoice == 'done'):
            print('Thanks for playing RPS with me ' + playerName)
            showStats()
            playRPS = False
            continue
        if(playerChoice == 'error'):
            print('Your choices are only 0 thru 3')
            continue
        else:
            codeChoice = determineRPS_str(random.randrange(1, 4))
            gameResults = determineRPS(playerChoice, codeChoice, playerName)
            print(gameResults)
            print(games)


#set global variable for play game
playGame = True

#this while block hands the user selection of how they want to plan the game
while (playGame):
    print('\n')
    print('------------------------------ Rock Scissors Paper ----------------------------')
    if playerName: 
        print('----------------  Current Player is ---> ' + playerName + ' ------------------')
    userChoice = getUserInput(
        '\n0 = end game \n1 = leader board \n2 = play \n3 = change player \n\nEnter Your Choice ')
    if userChoice == 0:
        playGame = False
    elif userChoice == 1:
        leaderBoard()
    elif userChoice == 2:
        userPlays()
    elif userChoice == 3:
        if not playerName:
            print('---------------------- No current player, select 2 to play ---------------')
        else:
            playerName = False    
    else:
        print('incorrect input')

print('---------------------------- Have a GREAT DAY!! ------------------------------')

