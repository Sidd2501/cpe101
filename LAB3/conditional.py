# Lab 3
#
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06


# This function takes in two numbers and compiles to see which number is larger.
# float, float -> float
def max_101(num1, num2):
    if num1 > num2:
        return num1
    elif num2 > num1:
        return num2
    else:
        return "Error"


# This function takes in three numbers and compiles to see which number is the largest.
# float, float, float -> float
def max_of_three(num3, num4, num5):
    if num3 < num4 < num5:
        return num5
    elif num4 < num3 < num5:
        return num5
    elif num4 < num5 < num3:
        return num3
    elif num5 < num4 < num3:
        return num3
    elif num5 < num3 < num4:
        return num4
    elif num3 < num5 < num4:
        return num4


# This function takes in a parameter stating the number of days and based on that, charges a late rental fee.
# float -> float
def rental_late_fee(days):
    fee = 0
    if days <= 0:
        fee = 0
    elif days <= 9:
        fee = 5
    elif days <= 15:
        fee = 7
    elif days <= 24:
        fee = 19
    else:
        fee = 100
    return fee
