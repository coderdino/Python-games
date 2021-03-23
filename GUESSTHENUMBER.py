#-------------------------------------------------------------------------------
# Name:         GUESSTHENUMBER
# Purpose:      To guess a number from 1 - 100
#
# Author:      Vaibhav
#
# Created:     20/03/2021
# Copyright:   (c) Vaibhav 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
__author__ = 'Vaibhav D Games'
# guess a number between 1 and 100 in ten tries
import random
answer = 'yes'
while answer == "yes":
    NumToGuess = random.randint(1, 100)
    NumOfTry = 10
    print ("Try to guess a number between 1 and 100 in 10 tries")
    while NumOfTry != 0:
        try:
            x = int (input ("Please enter a number between 1 and 100: "))
            if x > NumToGuess:
                print (x,"is too high")
                NumOfTry = NumOfTry - 1
                print (NumOfTry, "attempt(s) left")
                print ("")
            elif x < NumToGuess:
                print (x,"is too low")
                NumOfTry = NumOfTry - 1
                print (NumOfTry, "attempt(s) left")
                print ("")
            elif x == NumToGuess:
                print ("You Win, Congratulations!!!")
                NumOfTry = 0
        except:
            print ("Please enter a valid integer.")
            print("Remember, there is no way to cheat!")
    else:
        print ("The number to guess was: ", NumToGuess)
        answer = input ('Do you want to play again? (yes/no)')
else:
    print ("Thank you for playing. Goodbye")
