# Importing Tkinter module
from tkinter import *
from PIL import ImageTk, Image
import os
import random
import time
from collections import defaultdict

# Creating master Tkinter window
root = Tk()

# Global list for tracking games outcomes - 'win', 'loss', 'tie'
games = []

frame = LabelFrame(root, foreground="white", text="Rock, Scissors, Paper",
                   padx=100, pady=100)
frame.pack(padx=10, pady=10)
frame.configure(background='black')


def playRPS(playerChoice, gameChoice, player):
    resultOutput = Label(frame, text='')
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
    resultOutput = Label(frame, text=outputMessage)
    resultOutput.grid(row=3, column=0, columnspan=3)
    # Add result to game.txt

    games.append(result)
    writeToFile(player, result)


def writeToFile(player, result):
    dirname, filename = os.path.split(os.path.abspath(__file__))

    try:
        game_file = open(dirname + '/games.txt', 'a')
        game_file.writelines(player + ' ' + result + "\n")
        game_file.close()
    except IOError:
        print('Error while writing to file')


def readFile():
    # determine dirname of game.txt
    dirname, filename = os.path.split(os.path.abspath(__file__))

    # declare empty list
    games = []
    filepath = dirname + '/games.txt'

    # open
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
    # read games.text into memory
    games = readFile()
    if len(games) > 0:
        # filter by str 'win' to get all wins out of games.txt
        win = list(filter(lambda x: x[1] == 'win', games))

        # setup data dictonary
        winLeader = defaultdict(int)

        # for each entry in win count by player
        for player in win:
            winLeader[player[0]] += 1

        # Display to User
        print('---------------- Current Leader Board by games WON!!!! \
               ---------------------\n')
        # print({k: v for k, v in sorted(
        #    winLeader.items(), key=lambda item: item[1], reverse=True)})
        lb = sorted(winLeader.items(), key=lambda item: item[1], reverse=True)
        lbTitle = Label(frame, bg="blue", padx=10, pady=20,
                        text="Leader Board for Wins").grid(row=4, column=0,
                                                           columnspan=3)
        lbrow = 5
        for entry in lb:
            lbEntry = str(entry[0]) + " " + str(entry[1])
            lbRow = Label(frame, bg="green", text=lbEntry).grid(row=lbrow,
                                                                column=0,
                                                                columnspan=3)
            lbrow = lbrow + 1

    else:
        print('No data in game file')


def quitRPS():
    for widget in frame.winfo_children():
        widget.destroy()
    getEmail()


def showGame(email):
    gameChoice = random.choice(['rock', 'scissors', 'paper'])
    title = Label(frame, text="Play RPS " + email).grid(row=0, column=0,
                                                        columnspan=3)
    rock_button = Button(frame, text="rock", highlightbackground="#f0547d",
                         fg="black", height=10, width=15,
                         command=lambda: playRPS('rock', gameChoice,
                                                 email)).grid(row=2, column=0)
    scissors_button = Button(frame, text="scissors", height=10, width=15,
                             command=lambda: playRPS('scissors', gameChoice,
                                                     email)).grid(row=2,
                                                                  column=1)
    paper_button = Button(frame, text="paper", height=10, width=15,
                          command=lambda: playRPS('paper', gameChoice,
                                                  email)).grid(row=2, column=2)
    quit_button = Button(frame, text="QUIT", height=5, width=5,
                         command=quitRPS).grid(row=4, column=0, columnspan=3)


def checkEmail(email):
    if (re.match(r'[\w-]{1,20}@\w{2,20}\.\w{2,3}$', email)):
        for widget in frame.winfo_children():
            widget.destroy()
        showGame(email)
    else:
        error = Label(frame, bg="red", text="Incorrect Email, try again")
        error.grid(row=3, column=0, columnspan=3)


def getEmail():
    title = Label(frame,  text="Input Email to Play ")
    title.grid(row=0, column=1)
    e = Entry(frame, width=35, borderwidth=5)
    e.grid(row=1, column=1)
    button = Button(frame, width=5, height=2, text="Play",
                    command=lambda: checkEmail(e.get()))
    button.grid(row=2, column=1)
    leaderBoard()


getEmail()

root.mainloop()
