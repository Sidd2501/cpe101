# Lab 4
#
# Name:
# Instructor: Sussan Einakian
# Section:

import driver


def letter(row, col):
    if col > 9:
        return 'O'
    else:
        return 'X'


if __name__ == '__main__':
    driver.comparePatterns(letter)