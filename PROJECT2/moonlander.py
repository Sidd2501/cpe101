# Project 2 - Moonlander
#
# Name: Sid Sharma
# Instructor: S. Einakian
# Section: 06

# This file initializes variables and then uses a combination of calling methods and a loop to simulate different
# user oriented moon landings.

from landerFuncs import *

elapsedTime = 0
fuelRate = 0
velocity = 0
acceleration = 0
gravity = 1.62

showWelcome()
altitude = getAltitude()
currentFuel = fuelAmount = fuel = getFuel()
print()
print("LM state at retrorocket cutoff")

while altitude > 0:
    if fuelAmount > 0:
        displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
        fuelRate = getFuelRate(currentFuel)
        acceleration = updateAcceleration(gravity, fuelRate)
        altitude = updateAltitude(altitude, velocity, acceleration)
        velocity = updateVelocity(velocity, acceleration)
        fuel = currentFuel = fuelAmount = updateFuel(fuel, fuelRate)
    else:
        print("OUT OF FUEL - Elapsed Time: %3d Altitude: %7.2f Velocity: %7.2f" % (elapsedTime, altitude, velocity))
        fuelRate = 0
        acceleration = updateAcceleration(gravity, fuelRate)
        altitude = updateAltitude(altitude, velocity, acceleration)
        velocity = updateVelocity(velocity, acceleration)
        fuel = currentFuel = fuelAmount = updateFuel(fuel, fuelRate)
    elapsedTime += 1

print()
print("LM state at landing/impact")
displayLMState(elapsedTime, altitude, velocity, fuelAmount, fuelRate)
print()
displayLMLandingStatus(velocity)
