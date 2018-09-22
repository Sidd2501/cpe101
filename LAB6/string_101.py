# Lab 6
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

from char import *


# String -> string.
# This function returns the rot13 encoding for any given character.
def str_rot_13(str1):
    answer = ''
    rotty = [char_rot13(s) for s in str1]
    s = answer.join(rotty)
    return s

# String -> string.
# This function takes two strings and replaces one character with another and gives a new string.
def str_translate_101(str1, c1, c2):
    list1 = []
    for i in str1:
        if ord(i) == ord(c1):
            list1.append(c2)
        else:
            list1.append(i)
    final = ''.join(list1)
    return final
