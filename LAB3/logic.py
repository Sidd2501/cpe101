# Lab 3
#
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06


# This function determines if a given number is even or not.
# float -> bool
def is_even(num1):
    return num1 % 2 == 0


# This function determines whether or not a given number is inside specified intervals.
# float -> bool
def in_an_interval(num2):
    return -2 <= num2 < 9 or 22 < num2 < 42 or 12 < num2 <= 20 or 120 <= num2 <= 127
