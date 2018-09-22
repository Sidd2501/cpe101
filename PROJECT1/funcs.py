# Project 1
#
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

from math import *


# This function takes in a float value in pounds and converts it to kilograms.
# float -> float
def poundsToKG(pounds):
    return pounds * 0.453592


# This function takes in an object as the input and returns the mass in kilograms of
# the object.
# String -> float
def getMassObject(object):
    if object == 't':
        return 0.1
    elif object == 'p':
        return 1.0
    elif object == 'r':
        return 3.0
    elif object == 'l':
        return 9.07
    elif object == 'g':
        return 5.3
    else:
        return 0.000


# This function takes in the distance and from that computes the velocity of the object.
# float -> float
def getVelocityObject(distance):
    return sqrt((9.8 * distance) / 2)


# This function computes the velocity of the skater using conservation of momentum.
# float, float, float -> float
def getVelocitySkater(massSkater, massObject, velocityObject):
    return (massObject * velocityObject) / massSkater
