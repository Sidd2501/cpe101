# Lab 4
#
# Name:
# Instructor: Sussan Einakian
# Section:

import driver


def letter(row, col):
    if col >= row:
        return 'W'
    else:
        return 'T'


if __name__ == '__main__':
    driver.comparePatterns(letter)