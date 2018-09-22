# Lab 4
#
# Name:
# Instructor: Sussan Einakian
# Section:

import driver


def letter(row, col):
    if row > 4:
        return 'S'
    elif row < 2:
        return 'S'
    if 3 <= col <= 6:
        return 'M'
    else:
        return 'S'


if __name__ == '__main__':
    driver.comparePatterns(letter)