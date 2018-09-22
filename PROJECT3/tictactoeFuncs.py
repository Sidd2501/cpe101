# Project 3 - Tic-Tac-Toe Simulator
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

from random import randrange


# This function takes in no parameter and also returns nothing, based on the user input, it calls a function to either
# play Tic-Tac-Toe with two players or as a computer.
# None -> None.
def play():
    play1 = welcome()
    board = createBoard()
    printBoard(board)
    board = clearBoard()
    if play1 == '1':
        withComputer(board)
    else:
        players(board)


# This function prints a welcome message to the user and asks the user if it wants to play against another player or
# the computer.
# None -> String.
def welcome():
    print("Welcome to this Tic-Tac-Toe Simulator.")
    print("Your goal is to line up 3 of your tics in either a line or a diagonal.")
    print("You will pick either X or O.")
    choice = ' '
    while not (choice == '1' or choice == '2'):
        choice = input("Do you wish to play against the computer(1) or another player(2)?: ")
        print("The board positions are as follows:")
        if not(choice == '1' or choice == '2'):
            print("Error, please pick either option 1 or 2.")
            choice = input("Do you wish to play against the computer(1) or another player(2)?: ")
    return choice


# This function is called once the user has mentioned how they would like to play, against a computer or the player.
# It contains a while loop that calls other functions as well based on the letter the user picks for him(her)self.
# List -> None.
def withComputer(board):
    playerTurn = True
    playerLetter = pickLetter()
    if playerLetter == 'X':
        computerLetter = 'O'
    else:
        computerLetter = 'X'
    turn = 0
    game = True
    while game:
        if playerTurn:
            board = getInputC(playerLetter, board)
            turn = turnCount(turn)
            playerTurn = False
        else:
            board = computerMove(computerLetter, board)
            turn = turnCount(turn)
            playerTurn = True
        printBoard(board)
        game = checkWin(board)


# This function is in charge of getting the letter and using the board as a list to call other functions and print the
# board each time, update the board, and check to see if the user/other player/computer has won the game.
# List -> None.
def players(board):
    letter = pickLetter()
    game = True
    while game:
        getInput(letter, board)
        letter = turnCount(letter)
        printBoard(board)
        game = checkWin(board)


# This function creates a table specifying the location numbers of each cell, letting the user know where they can put
# their letters.
# None -> List.
def createBoard():
    board = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
    return board


# This function empties the table after the location numbers of each cell have been specified, showing the user where
# they can place their letter on the board.
# # None -> List.
def clearBoard():
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    return board


# This function creates an empty table so that the user can know where they can put their letters.
# their letters.
# None -> List.
def printBoard(board):
    index = 0
    for i in range(0, 3):
        print('' + board[index] + ' | ' + board[index + 1] + ' | ' + board[index + 2])
        index += 3
        print('----------')


# This function allows the user to pick a valid letter in order to play the game of tic-tac-toe.
# None -> String.
def pickLetter():
    letter = ''
    while not(letter == 'X' or letter == 'O'):
        letter = input("Do you want to be X or O?: ")
        if not(letter == 'X' or letter == 'O'):
            print("Error. Please select the correct letter.")
            letter = input("Do you want to be X or O?: ")
    return letter


# This function shows the user that the computer has made a move and where it placed its letter.
# String, List -> List.
def computerMove(letter, board):
    move = 0
    while isSpaceFree(board, move):
        move = randrange(1, 10)
    print('Computer (' + letter + ') makes a move.')
    board[int(move) - 1] = letter
    return board


# This function allows the user to type in their move given the constraints.
# String, List -> List.
def getInput(letter, board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        move = input(
            'Player with letter ' + letter + ', where would you like to place your letter (pick in range of 1-9)'
                                             ': ')
        if move not in '1 2 3 4 5 6 7 8 9'.split():
            print('Invalid value! Enter a valid number between 1 and 9.')
        elif isSpaceFree(board, int(move)):
            print('Invalid move! Location is already taken. Please try again.')
            move = ''
        else:
            board[int(move) - 1] = letter
    return board


# This function allows the user to type in their move given the constraints. This is for the
# computer mode specifically.
# String, List -> List.
def getInputC(letter, board):
    move = ' '
    while move not in '1 2 3 4 5 6 7 8 9'.split() or not isSpaceFree(board, int(move)):
        move = input(
            'Player with letter ' + letter + ', where would you like to place your letter (pick in range of 1-9'
                                             '): ')
        if move not in '1 2 3 4 5 6 7 8 9'.split():
            print('Invalid value! Enter a valid number between 1 and 9.')
        elif isSpaceFree(board, int(move)):
            print('Invalid move! Location is already taken. Please try again.')
            move = ' '
        else:
            board[int(move) - 1] = letter
    return board


'''# Given a board and the computer's letter, this function determines where to move and return
# that move.
# List, String -> None.
def getComputerMove(board, computerLetter):
    if computerLetter == 'X':
        playerLetter = 'O'
    else:
        playerLetter = 'X'''''


# This function checks the board to see if either player has won by checking if there are X's or O's in each row.
# List -> Bool.
def checkRows(board):
    if board[0] == board[1] and board[0] == board[2] and board[0] != ' ' and board[1] != ' ' and board[2] != ' ':
        return True, board[0]
    elif board[3] == board[4] and board[3] == board[5] and board[3] != ' ' and board[4] != ' ' and board[5] != ' ':
        return True, board[3]
    elif board[6] == board[7] and board[6] == board[8] and board[6] != ' ' and board[7] != ' ' and board[8] != ' ':
        return True, board[6]
    else:
        return False, ' '


# This function checks the board to see if either player has won by checking if there are X's or O's in each column.
# List -> Bool.
def checkCols(board):
    if board[0] == board[3] and board[0] == board[6] and board[0] != ' ' and board[3] != ' ' and board[6] != ' ':
        return True, board[0]
    elif board[1] == board[4] and board[1] == board[7] and board[1] != ' ' and board[4] != ' ' and board[7] != ' ':
        return True, board[1]
    elif board[2] == board[5] and board[2] == board[8] and board[2] != ' ' and board[5] != ' ' and board[8] != ' ':
        return True, board[2]
    else:
        return False, ' '


# This function checks the board to see if either player has won by checking if there are X's or O's in each diagonal.
# List -> Bool.
def checkDiags(board):
    if board[0] == board[4] and board[0] == board[8] and board[0] != ' ' and board[4] != ' ' and board[8] != ' ':
        return True, board[0]
    elif board[2] == board[4] and board[2] == board[6] and board[2] != ' ' and board[4] != ' ' and board[6] != ' ':
        return True, board[2]
    else:
        return False, ' '


# This function returns True if every space on the board has been taken. Otherwise, it
# returns False. It checks to see if the board location is taken.
# List -> Bool.
def boardFull(board):
    for i in range(1, 10):
        if not isSpaceFree(board, i):
            return False
    return True


# This function gets the board as the parameter and checks to see if any rows/columns/diagonals
# match, then, it prints who won the game.
# List -> Bool.
def checkWin(board):
    if checkRows(board)[0]:
        print(checkRows(board)[1], "is the winner!")
        return False
    elif checkCols(board)[0]:
        print(checkCols(board)[1], "is the winner!")
        return False
    elif checkDiags(board)[0]:
        print(checkDiags(board)[1], "is the winner!")
        return False
    elif boardFull(board):
        print('Game is a draw!')
        return False
    else:
        return True


# This function makes sure that if the user's turn is uses 'X', the opposite must return 'O.'
# List, int -> String.
def turnCount(turn):
    print("It's Player " + str(turn) + "'s turn:")
    if turn == 'X':
        return 'O'
    else:
        return 'X'


# This function returns True if the passed move is free on the passed board. It lets the
# user know that the location they are trying to move to, is free.
# List, int -> String.
def isSpaceFree(board, move):
    return board[move - 1] == 'X' or board[move - 1] == 'O'
