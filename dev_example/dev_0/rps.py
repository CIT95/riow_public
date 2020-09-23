""" 
Rock Scissors Paper (RPS) games
This program will use a simple menu to allow the player to play RPS or 
have the game play RPS.  

If the user selects human play, then they are presented with another menu 
to select their RPS choice or stop playing.  If user selects stop playing then they are shown statistics for their game play and return to beginning menu. 

If the user selects game play, then the code will determine a random number of times to play and use the funciton setup for human play and output statistics after the number of games is complete 

"""
# import random from standard library
import random

# Global list for tracking games outcomes - 'win', 'loss', 'tie'
games = []

# function to determine the outcomes of a RSP game
# returns str and updates global list for tracking game outcomes

def determineRPS(playerChoice, gameChoice):
    if playerChoice == gameChoice:
        games.append('tie')
        return 'Tie'
    if playerChoice == 'rock':
        if gameChoice == 'scissors':
            games.append('win')
            return 'Rock beats Scissors - Player Wins'
        else:
            games.append('loss')
            return 'Scissors beats Paper - Game Wins'
    if playerChoice == 'paper':
        if gameChoice == 'rock':
            games.append('win')
            return 'Paper beats Rock - Player Wins'
        else:
            games.append('loss')
            return 'Scissors cuts Paper - Game Wins'
    if(playerChoice == 'scissors'):
        if(gameChoice == 'paper'):
            games.append('win')
            return 'Scissors Cut Paper = Player Wins'
        else:
            games.append('loss')
            return 'Rock crushes Scissors -  Game Wins'

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

#function handles the user selection of game play


def gamePlays():
    print('------------------------------------Game Plays-------------------------------')
    numGames = random.randrange(1, 11)
    for i in range(1, numGames):
        gameChoice1 = determineRPS_str(random.randrange(1, 4))
        gameChoice2 = determineRPS_str(random.randrange(1, 4))
        gameResults = determineRPS(gameChoice1, gameChoice2)
        print(gameResults)
        print(games)

    showStats()

# function show game play statistics


def showStats():
    global games
    print('--------------------------------Game Statics here----------------------------------')
    print('Total Games Played ' + str(len(games)))
    print('Player won ' + str(games.count('win')))
    games = []

# function handles the user playing RPS as many times as they like and once they select 0 to stop they are
# shown game statistics


def userPlays():
    playRPS = True
    playerName = input('Player Name ')
    while(playRPS):
        print(
            '----------------------------------- Human Plays -------------------------------')
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
            gameResults = determineRPS(playerChoice, codeChoice)
            print(gameResults)
            print(games)


#set global variable for play game
playGame = True

#this while block hands the user selection of how they want to plan the game
while (playGame):
    print('\n')
    print('------------------------------ Rock Scissors Paper ----------------------------')
    userChoice = getUserInput(
        '0 = end game \n1 = game plays \n2 = human plays\nEnter Your Choice ')
    if userChoice == 0:
        playGame = False
    elif userChoice == 1:
        gamePlays()
    elif userChoice == 2:
        userPlays()
    else:
        print('incorrect input')

print('-----------------------------------Have a GREAT DAY!!-----------------------------')
