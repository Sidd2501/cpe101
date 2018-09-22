# Lab 6
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

from functools import reduce


# list -> int.
# This function sums up all the elements in a list.
def sum(L1):
    return reduce(lambda x, y: x + (sum(y) if isinstance(y, list) else y), L1)


# list -> int.
# This function returns the index of the smallest element in a list.
def index_of_smallest(L2):
    if len(L2) > 0:
        smallest_index = 0
        for index in range(1, len(L2)):
            if L2[index] < L2[smallest_index]:
                smallest_index = index
        return smallest_index
    else:
        return -1
