#Lab 2 Functions
#Name: Sid Sharma
#Section: 06

from math import *

#This function will take in two integers and performs a specific mathematical
#computation.
#int int -> float
def math_func1(x, y):
    return (x**3 + y**3) / (5*x + 7)

#This function takes in 3 integers and performs the quadratic formula.
#int int int -> float
def math_func2(a, b, c):
    return (-b + sqrt(b**2 - (4*a*c))) / (2*a)

#This function computes the Euclidean distance between two points.
#int int int int -> float
def d(x1, y1, x2, y2): 
    return sqrt((x1-x2)**2 + (y1-y2)**2)

#This function takes in a single integer and outputs a boolean value based on
#the sign of the integer.
#int -> bool
def is_negative(n):
    return n < 0
    
#This function tests if an integer is divisible by 5.
#int -> bool
def dividable_by_5(q):
    return -(q % 5)
