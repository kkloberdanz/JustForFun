#!/usr/bin/python3

"""
Programmer: Kyle Kloberdanz
Date      : 2 Dec 2015

Directions: 
            This is a program that reads in a quadratic formula 
            like this './quadratic 12x^2 - 100x + 20000'
            and returns the solutions to x
            (Ensure there are spaces between '+' and coeficcients)
            
            Plus signs are implied, and are not needed
            This program only accepts integers 
"""

import sys

# I'm using my implementation of squareRoot rather than the math library
# because I plan to implement non-real solutions in the future, and this
# implementation of square root can deal with imaginary numbers
def squareRoot(s,e = 0):
    '''
    Title: squareRoot
    Description: takes in a number and how much error desired, and returns the sqrt
    Inputs: s --> The number one wishes to square root
            e --> Epsilon, the amount of error tolllorated
    Outputs: sqrt --> square root of the input (s)
    Note: uses Babylonian Method
    '''
    guess = s/5
    if (s < 0): # For imaginary numbers
        s = s * -1
    sqrt = s

    while( abs(guess - sqrt) > e):
            guess = sqrt
            sqrt = (guess + (s/guess))/2
    return (sqrt)

a = 0
b = 0
c = 0

aIsNegative = False
bIsNegative = False
cIsNegative = False

# Removes 'quadratic' from argv
equation = sys.argv[1:]

nextItemIsNegative = False
for item in equation:

    # if current item is '-', then next item is a number
    # that is being subtracted
    if item == "-":
        nextItemIsNegative = True

    elif "x^2" in item:
        if item[0] == 'x':
            a = 1
        else:
            a = int(item[0:item.index('x')])
            if nextItemIsNegative:
                aIsNegative = True
                nextItemIsNegative = False

    elif "x" in item:
        if item[0] == 'x':
            b = 1
        else:
            b = int(item[0:item.index('x')])
            if nextItemIsNegative:
                bIsNegative = True
                nextItemIsNegative = False

    elif "x" not in item and item != "+":
        # constant term
        if item[0] == 'x':
            b = 1
        else:
            c = int(item)
            if nextItemIsNegative:
                cIsNegative = True
                nextItemIsNegative = False

if aIsNegative:
    a = -1 * a
if bIsNegative:
    b = -1 * b
if cIsNegative:
    c = -1 * c


if a == 0:
    print("a == 0, This equation is NOT quadratic")
    sys.exit()

innerArg = b**2 - 4 * a * c
squareRT = squareRoot(innerArg)

if innerArg < 0:
    # Non-real sollution
    print( "x = "+str(-b/(2*a) ) +" +/- "+ str(squareRT/(2*a))+ " i" )

else: 

    root1 =  (-b + squareRT) / (2 * a )
    root2 =  (-b - squareRT) / (2 * a )

    print( "x =",  str(root1) )
    print( "x =",  str(root2) )
