# Project 3 - Tic-Tac-Toe Simulator
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

# This file initializes variables and then uses a combination of calling methods and loops to allow the user to play
# Tic-Tac-Toe either against a player or the computer.

from tictactoeFuncs import *

play1 = welcome()
board = createBoard()
printBoard(board)
board = clearBoard()
if play1 == '1':
    withComputer(board)
else:
    players(board)
    playerTurn = True
