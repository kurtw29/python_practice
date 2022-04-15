#my first attempt to write guess the Number program
# guess the number game, while keep track of guess attemped.

import random

# intro and generate the correct answer, random # between 1 and 20
print("I'm thinking of a number between 1 and 20.")
attempts = 0
correctNum = random.randint(1,20)
#print("corerctNum = "+ str(correctNum)) #print correct answer during testing phase, comment out after complete

def guess():    #call function to guess number again; there's cleaner way to do this w/o creating a guess() function
    print("Take a guess.")
    global attempts             #resolve local & global scope issue for 'attempts' variable
    attempts = attempts + 1     #keep track of guess attempts
    global guessNum             # resolve local & global scope for guess number (to be evaluated out of the guess function)
    try:                        # in case someone type non-integer number and throws an error
        guessNum = int(input())
    except ValueError:
        print("Error: Please enter an integer") #provide instruction to resolve error and re-do the guess
        guess()
        
guess() #start getting
while guessNum != correctNum:   #evaluate guess result & keep guessing until guess the correct number
    print("guessing attempts: "+ str(attempts))
    if guessNum > correctNum:
        print("Your guess is too high")
    elif guessNum < correctNum:
        print("Your guess is too low")
    guess()

if guessNum == correctNum:  #when guessed the correct number
    print("Good job! You guessed my number in "+str(attempts)+" guesses!")
