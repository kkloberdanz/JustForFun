# Programmer: Kyle Kloberdanz
# Date Created: 23 May 2015
# Description: This program tests the user in multiplication
#              and percentages               

import random
import time 

def percentError(guess, exact):
    """
    Calculates and returns the percentage error
    """
    return abs(((guess - exact) / exact) * 100)

def multiplication():
    """
    Tests user on multiplication abilities
    """
    
    # Counter to track the number of successful user answers
    numCorrect = 0    
    
    # Change this to change the number of rounds to go through.
    numberOfRounds = 10

    # Change to allow a different percentage error
    tollerablePercentError = 10



    print("Select how many digits you want to limit the numbers to")

    try:
        numDigits = int(input("Select: 1, 2, 3, or 4\n"))
        if numDigits < 1 or numDigits > 4:
            print("That is not a valid option")
            return None

    except:
        print("Not a valid option")
        return None

    startTime = time.time()
    
    print("Ok, you will now be tested on", numDigits, "digit numbers")
    print("(Press CTRL-d to quit)\n")

    i = 1
    while i <= numberOfRounds:


        if numDigits == 1:
            num1 = random.randint(1, 9)
            num2 = random.randint(1, 9)

        elif numDigits == 2:
            num1 = random.randint(1, 99)
            num2 = random.randint(1, 99)

        elif numDigits == 3:
            num1 = random.randint(1, 999)
            num2 = random.randint(1, 999)

        elif numDigits == 4:
            num1 = random.randint(1, 9999)
            num2 = random.randint(1, 9999)

        else:
            print("That feature is not available")
            return None 


        actual_ans = num1 * num2

     
        print("\n------- Round", i, "-------")
    
        # Ask the user to multiply two random ints, 
        # then recieve user input
        print("\nWhat is", num1, "X", num2)
        try:
            user_ans = int(input(">>> "))
        except:
            print("That is not a valid input")
            return None

        if user_ans == actual_ans:
            print("Spot on! You are exactly right!")
            numCorrect += 1

        elif percentError(user_ans, actual_ans) <= tollerablePercentError:

            print("Close enough! The exact answer is:", actual_ans)

            print("Your percent error is:", 
                    percentError(user_ans, actual_ans), "%")

            numCorrect += 1

        else:
            print("Sorry honey :( Your percentage error is:", 
                    percentError(user_ans, actual_ans), "%")

            print(num1, "X", num2, "=",  actual_ans)

        i += 1

    print("You have scored:", numCorrect, "out of", i - 1)



def percentages():
    """
    Tests user on abilities of multiplying percentages
    """

    # Change this to allow a different percent error
    tollerablePercentError = 10

    # Change to alter the number of rounds to play
    numRounds = 10

    # Counter that keeps track up correct user answers
    numCorrect = 0

    i = 1
    while i <= numRounds:
    
        # Used to force the answer to be correct if the user
        # input is arbitarily close to the correct answer
        # (Needed because floats behave weirdly)
        forcePass = False

        # Randomly generate a percentage and a number to multiply it by
        percent = random.randint(1, 99)/100
        num = random.randint(1, 1000)

        # Actual solution to problem
        actual_ans = percent * num

        print("\n------- Round", i, "-------")

        print("\n\nWhat is", percent*100, "% of", num)
        try:
            user_ans = float(input(">>> "))
        except:
            print("That is not a valid input")
            return None

        # Incase there is a problem where the float is not correct
        if percentError(user_ans, actual_ans) < 0.00001:
            forcePass = True

        # Perfect answer
        if user_ans == actual_ans or forcePass:
            print("Spot on! You are exactly right!")
            numCorrect += 1

        # Acceptable anser
        elif percentError(user_ans, actual_ans) <= tollerablePercentError:
            print("Close enough! The exact answer is:", actual_ans)
            print("Your percent error is:", 
                    percentError(user_ans, actual_ans), "%")
            numCorrect += 1

        # Unacceptable answer
        else:

            print("Sorry honey :( Your percentage error is:", 
                    percentError(user_ans, actual_ans), "%")

            print(percent*100, "% of", num, "is", actual_ans)

        i += 1

    print("You have scored", numCorrect, "out of", i - 1)


############################## BEGIN MAIN ##############################
user_input = ""

while True:

    # Break from while
    if user_input == "quit":
        break

    print("\n\nWelcome Ellie, to your math tutorial :)")
    print("(type quit to quit)")
    user_input = input("\nType m for multiplication or p for percentages\n")

    if user_input == "m":
        multiplication()

    elif user_input == "p":
        percentages()
