# Programmer: Kyle Kloberdanz
# Section: CS:1210:0A04 
# hawkID: 00798167
# Program: misc_functions
# Note: This is the list of functions I have created since I began the
#       the class: CS 1: Fundementals at the University of Iowa. If you
#       have stumbled apon this set of functions, feel free to use them,
#       but please include my name as the programmer in the
#       comment blocks. Cheers!

def exponent(b,e):
    '''
    Title: exponent
    Description: takes in a base and an exponent to compute an exponential problem
    Inputs: b --> base 
            e --> exponent
    Outputs: ans --> answer
    '''
    ans = b
    i = 1
    
    if e == 0:
        return 1
    
    while i < e:
        ans = b * ans
        i = i + 1    
    return (ans)

def factorial(fact):
    '''
    Programmer: Kyle Kloberdanz
    Title: factorial
    Description: takes in a number and computes the factorial of said number.
    Inputs: fact --> the number to factorialize
    Outputs: ans --> answer
    '''
    ans = fact
    i = 1
    while i < fact:
        ans = ans * i
        i = i + 1
    return(ans)

    # end of function factorial

def squareRoot(s,e):
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
            return (str(sqrt) + " i")                

    else:
            sqrt = s
    
            while( abs(guess - sqrt) > e):
                    guess = sqrt
                    sqrt = (guess + (s/guess))/2
            return (sqrt)

    # end of function 
     
def root(n,r):
    '''
    Programmer: Kyle Kloberdanz
    Function title: root
    Description: takes in a number and how much error desired, and returns the ans
    Inputs: n --> The number one wishes to root
            r --> The desired root one wishes to solve
    Outputs: ans --> n to the root r
    Note: uses Babylonian Method
    '''
    e = 0
    guess = n/5
    ans = n
    timeOut = 10000 # Keeps the program from looping indefinitely
    i = 0
        
    while( abs(guess - ans) > e) and (i <= timeOut):
        guess = ans
        ans = ( ( (r-1) * guess ) + (n/( guess ** (r-1) ) ) )/r
        i = i + 1
    
    if i >= timeOut:
        print("\nERROR, function has timed out.\nThe answer may not be accurate.")

    print("Number of iterations: ",i)

    return (ans)

    # end of function: root

def isPrime(n):
    '''
    Programmer: Kyle Kloberdanz
    Funciton name: isPrime
    input : n --> number that will be tested if prime.
            If n is not of type int, then this function will
            force it to be an int.
    output: prime --> type: bool, tells user if the number is prime
            i.e. returns True if prime, and False if composite.        
   '''
    import math
    
    n = int(n)
    
    prime = True

    # finding sqrt(n) speeds up the algorithm
    N = int( math.sqrt(n) + 1 )
    
    # N is the largest n value that will be tested.
    for i in range(2, N):
        if (n % i == 0):
            prime = False
            
    return( prime )

    # End function: isPrime
