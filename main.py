# Title: Guessing game
# Author: Juan Roldan

import random
import time

#generate random number
def generateRandom():
    randNumber = random.randint(1,100)
    print(">>>>",randNumber)
    print("Number Guessing Game--------------------")
    return randNumber

#user input function
def getUserInput(counter,numbersList):
    #flag used to validate user input
    validated = False
    while(validated == False):
        guess = input("Enter guess number #" + str(counter + 1) +  " between 1 and 100: ")
        #Validate number is digit
        if(guess.isdigit() != True):
            print("*** Invalid Input : Please try again...")
            validated = False
        # if its digit but is in the list
        elif(int(guess) in numbersList):
            print("*** Incorrect Input: Repeated number")
            validated = False
        # if its digit is not in the list and is in range
        elif(int(guess)>=1 and int(guess)<=100):
            guess = int(guess)
            numbersList.append(guess)
            validated = True
        #if it is not in range
        else:
            print("*** Incorrect Input: Must be in range from 1 and 100")
            validated = False
                    
    return guess

#function that validates number, used in the process funtion
def validateNumber(number, randNumber):
    
    #means next guess should be lower
    if number > randNumber:
        return 1
    #means next guess should be lower
    elif number < randNumber:   
        return -1
    #means user won
    else:
        return 0

#function that calculates if next guess should be higher or lower
def process(number,randNumber,counter):
    endGame=0
    #if number is guessed
    if(validateNumber(number,randNumber)==0):
        print("Guess #",counter," : ",number,"CORRECT!")
        print("YOU WIN!")
        endGame=1
        time.sleep(2)
    #if next guess should be lower and still not 10 guesses
    elif (validateNumber(number,randNumber)==1 and counter<10):
        print("Guess #",counter," : ",number,"- Lower!")
        print("----------------------------------------")
    #if next guess should be higher and still not 10 guesses
    elif (validateNumber(number,randNumber)==-1 and counter<10):
        print("Guess #",counter," : ",number,"- Higher!")
        print("----------------------------------------")
    #if counter is over 10
    else:
        print("GAME OVER!!!!!!!!!!")
        endGame=1
        time.sleep(2)
    return endGame

def main():
    #get target number
    randNumber = generateRandom()
    
    #variable value that will never change
    flag=0
    
    #variable to count number of guesses
    counter=0
    
    #declare list to store numbers used
    #declared here because if it is declared in input function the list will be resetted every time user inputs anything validated 
    numbersList = []

    #while loop will go on since flag never changes
    while(flag==0):
        number = getUserInput(counter,numbersList)
        counter = counter + 1
        #calculates if next guess must be higher or lower and if game has ended
        endGame = process(number, randNumber,counter)
                #if game has ended reset all
        if(endGame == 1):
            randNumber = generateRandom()
            counter=0
            numbersList = []
main()
