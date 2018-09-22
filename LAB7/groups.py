# Lab 7
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06


# This function splits a given list into sub-lists with 3 maximum elements.
def groups_of_3(L1):
    return [L1[idx:idx + 3] for idx in range(0, len(L1), 3)]
