# Project 2 - Moonlander
#
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

# This function displays a welcome courtesy message to the user when it is called.
# None -> None.
def showWelcome():
    print("Welcome aboard the Lunar Module Flight Simulator")
    print()
    print("   To begin you must specify the LM's initial altitude")
    print("   and fuel level.  To simulate the actual LM use")
    print("   values of 1300 meters and 500 liters, respectively.")
    print()
    print("   Good luck and may the force be with you!")
    print()


# This function asks the user to input the initial amount of fuel in liters, which is an integer. It also uses a
# loop to deal with certain exceptions.
# None -> int.
def getFuel():
    fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    while fuel <= 0:
        print('Error! Please enter a valid non-zero, positive value.')
        fuel = int(input("Enter the initial amount of fuel on board the LM (in liters): "))
    return fuel


# Similar to the previous function, this function asks the user to input the initial altitude in meters, which
# is an integer. It also uses a loop to deal with certain exceptions.
# None -> int.
def getAltitude():
    alt = int(input("Enter the initial altitude of the LM (in meters): "))
    while alt < 1 or alt > 9999:
        print("Error! Please enter a valid number between 1 and 1999")
        alt = int(input("Enter the initial altitude of the LM (in meters): "))
    return alt


# This function simply prints the initial time, rate, and velocity which are set to 0 as well as the inputed
# values of fuel and altitude.
# int, float, float, int, int -> String.
def displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate):
    print("Elapsed Time: %4d" % int(elapsedTime) + " s")
    print("        Fuel: %4d" % int(fuelAmount) + " l")
    print("        Rate: %4d" % int(fuelRate) + " l/s")
    print("    Altitude: %7.2f" % float(altitude) + " m")
    print("    Velocity: %7.2f" % float(velocity) + " m/s")


# This function asks the user to input the fuel rate in liters, which is an integer between 0-9. It also uses a
# loop to deal with certain exceptions.
# int -> int.
def getFuelRate(currentFuel):
    print()
    currfuel = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    while currfuel < 0 or currfuel > 9:
        print("ERROR: Fuel rate must be between 0 and 9, inclusive")
        currfuel = int(input("Enter fuel rate (0-9, 0=freefall, 5=constant velocity, 9=max thrust): "))
    return min(currentFuel, currfuel)


# This function prints a message once the moonlander has landed based on the velocity value.
# int -> String.
def displayLMLandingStatus(velocity):
    if -1 <= velocity <= 0:
        print("Status at landing - The eagle has landed!")
    elif -10 < velocity < -1:
        print("Status at landing - Enjoy your oxygen while it lasts!")
    elif velocity <= -10:
        print("Status at landing - Ouch - that hurt!")


# This function updates the acceleration value based on what the user has been entering and what happens during
# the course of the moon-landing process.
# float, int -> float.
def updateAcceleration(gravity, fuelRate):
    return gravity * ((fuelRate / 5.0) - 1)


# This function updates the altitude value based on what the user has been entering and what happens during
# the course of the moon-landing process.
# float, float, float -> float.
def updateAltitude(altitude, velocity, acceleration):
    newalt = altitude + velocity + (acceleration / 2)
    if newalt >= 0:
        return newalt
    else:
        return 0


# This function updates the velocity value based on what the user has been entering and what happens during
# the course of the moon-landing process.
# float, float -> float.
def updateVelocity(velocity, acceleration):
    return velocity + acceleration


# This function updates the fuel value based on what the user has been entering and what happens during
# the course of the moon-landing process.
# int, int -> int.
def updateFuel(fuel, fuelRate):
    return fuel - fuelRate
