#my refactured version of the Guess the Number program
#Updated version:
    #remove the guess() function, guess number within the while loops
    #remove the global variable codes,
    #improve the "while" loop code

#guess the number game, while keep track of guess attemped,
#keep guessing until guess the right number,
#account for error input

import random

# intro and generate the correct answer, random # between 1 and 20
print("I'm thinking of a number between 1 and 20.")
attempts = 0
correctNum = random.randint(1,20)
#print("correctNum = "+ str(correctNum)) #print correct answer during testing phase, comment out after complete
        
while True:   #evaluate guess result & keep guessing, only guess the correct number will break the loop
#    print("guessing attempts: "+ str(attempts)) #keep track of attempts, to be comment-out after finish
    print("Take a guess.")
    attempts = attempts + 1     #keep track of guess attempts
    try:                        # in case someone type non-integer number and throws an error
        guessNum = int(input())
        if guessNum > correctNum:
            print("Your guess is too high")
        elif guessNum < correctNum:
            print("Your guess is too low")
        else:                   # when guessNum == correctNum exit out of while loop
            break
    except ValueError:
        print("Error: Please enter an integer") #provide instruction to resolve error

#Since out of while loop, the guess must be correct, so print result
print("Good job! You guessed my number in "+str(attempts)+" guesses!")
