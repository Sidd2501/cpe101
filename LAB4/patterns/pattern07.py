# Lab 4
#
# Name:
# Instructor: Sussan Einakian
# Section:

import driver


def letter(row, col):
    if 1 < row < 4 and 3 < col < 10:
        return 'Z'
    elif 3 < row < 6 and 3 < col < 7:
        return 'Z'
    elif 3 < row < 6 < col < 10:
        return 'X'
    elif 3 < row < 6 and 9 < col < 13:
        return 'B'
    elif row == 6 and 6 < col < 13:
        return 'B'
    else:
        return 'T'


if __name__ == '__main__':
    driver.comparePatterns(letter)
