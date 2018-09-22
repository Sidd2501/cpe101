# Lab 4
#
# Name:
# Instructor: Sussan Einakian
# Section:

import driver


def letter(row, col):
    if row > 9:
        return 'Q'
    else:
        return 'R'


if __name__ == '__main__':
    driver.comparePatterns(letter)
