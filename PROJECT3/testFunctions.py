# Project 3 - Tic-Tac-Toe Simulator
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

# The following file contains the unit tests for each of the I/O functions created in tictactoeFuncs.py.

import unittest
from tictactoe import *


class TestCases(unittest.TestCase):
    def test_checkRows(self):
        board4 = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertEqual(checkRows(board4), (False, ' '))
        board5 = ['X', 'X', 'X', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertEqual(checkRows(board5), (True, 'X'))
        board6 = ['X', ' ', ' ', 'X', ' ', ' ', 'O', 'O', 'O']
        self.assertEqual(checkRows(board6), (True, 'O'))

    def test_checkCols(self):
        board1 = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertEqual(checkCols(board1), (True, 'X'))
        board2 = ['X', ' ', ' ', 'X', ' ', ' ', 'O', ' ', 'O ']
        self.assertEqual(checkCols(board2), (False, ' '))
        board3 = ['O', ' ', ' ', 'O', ' ', ' ', 'O', ' ', ' ']
        self.assertEqual(checkCols(board3), (True, 'O'))

    def test_checkDiags(self):
        board7 = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertEqual(checkDiags(board7), (False, ' '))
        board8 = ['X', ' ', ' ', 'X', 'X ', 'X', 'X', ' ', 'X']
        self.assertEqual(checkDiags(board8), (True, 'X'))
        board9 = ['', '', 'O', '', 'O', '', 'O', '', '']
        self.assertEqual(checkDiags(board9), (True, 'O'))

    def test_boardFull(self):
        board12 = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'X']
        self.assertEqual(checkWin(board12), False)
        board13 = ['O', ' ', 'O', ' ', 'O', 'X', ' ', 'X', ' ']
        self.assertEqual(checkWin(board13), True)

    def test_checkWin(self):
        board10 = ['X', ' ', ' ', 'X', ' ', ' ', 'X', ' ', ' ']
        self.assertEqual(checkWin(board10), False)
        board11 = [' ', 'X', ' ', ' ', ' ', 'X', 'X', ' ', ' ']
        self.assertEqual(checkWin(board11), True)

    def test_turnCount(self):
        board14 = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'X']
        self.assertEqual(checkWin(board14), False)
        board15 = [' ', ' ', ' ', ' ', ' ', 'X', ' ', ' ', ' ']
        self.assertEqual(checkWin(board15), True)

    def test_isSpaceFree(self):
        board16 = ['O', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'X']
        self.assertEqual(checkWin(board16), False)
        board16 = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
        self.assertEqual(checkWin(board16), True)


# Run the unit tests.
if __name__ == '__main__':
    unittest.main()
