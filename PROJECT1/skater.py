# Project 1
#
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

from funcs import *


def main():
    pounds = float(input("How much do you weigh (pounds)? "))
    distance = float(input("How far away is your professor (meters)? "))
    object = str(input("Will you throw a rotten (t)omato, banana cream (p)ie, (r)ock, (l)ight saber, or lawn (g)nome? "))
    print()
    velocitySkater = round(getVelocitySkater(poundsToKG(pounds), getMassObject(object), getVelocityObject(distance)), 3)

    if getMassObject(object) <= 0.1:
        print("Nice throw! You're going to get an F!")
    elif 0.1 < getMassObject(object) <= 1.0:
        print("Nice throw! Make sure your professor is OK.")
    elif getMassObject(object) > 1.0 and getVelocityObject(distance) > 20.0:
        print("Nice throw! How far away is the hospital?")
    elif getMassObject(object) > 1.0 and getVelocityObject(distance) <= 20.0:
        print("Nice throw! RIP professor.")

    print("Velocity of skater: %.3f" % velocitySkater, "m/s")
    if velocitySkater < 0.2:
        print("My grandmother skates faster than you!")
    elif 0.2 <= velocitySkater < 1.0:
        print("")
    elif velocitySkater >= 1.0:
        print("Look out for that railing!!!")
    elif velocitySkater == 0:
        return 0.000


if __name__ == '__main__':
    main()
