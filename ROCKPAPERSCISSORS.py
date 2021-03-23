#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      d9dachavaram
#
# Created:     19/03/2020
# Copyright:   (c) d9dachavaram 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import time
from time import sleep
import random

print("Hello! Welcome to rock, paper, scisscors")

bet = int(input("How much money are you going to bet?"))

sus="-"*35
depo=["rock","paper","scissors"]
while True:
    x=input("Pick one: rock , paper, scissors: ")
    if x not in depo:
        print ("Dont cheat!")
        continue

    pc=random.choice(depo)
    sleep(0.5)
    print (("Computer picked {}.").format(pc))
    if x==pc:
        sleep(0.5)
        print (("\nIt's a draw.\n{}").format(sus))
        print ("You won half of your bet:", bet/2)
    elif x=="rock" and pc=="scissors":
        sleep(0.5)
        print (("\nYou win. Rock beats scissors\n{}").format(sus))
        print("You won:", bet)
    elif x=="paper" and pc=="rock":
        sleep(0.5)
        print (("\nYou win. Paper beats rock\n{}").format(sus))
    elif x=="scissors" and pc=="paper":
        sleep(0.5)
        print (("\nYou win. Scissors beats paper\n{}").format(sus))
        print("You won:", bet)
    else:
        sleep(0.5)
        print (("\nYou lose. {} beats {}\n{}").format(pc,x,sus))
        print("You Lose:", bet)
input()