""" Colin O'Connor 5/2/2023
Mastermind Project
A project that emulates the game of mastermind using lists
and random numbers to simulate the person with the colors
the computer uses the input numbers to provide clues after it checks with the guess
"""

import random
ALL_COLORS = ['red','orange','yellow','green','blue','purple']
#Resets the game if the player wants to by calling the gameplay
def reset():
    question = input("Would you like to play again? (Y/N)")
    if(question == 'n' or question == 'N'):
        print("Thank you for playing. Good-bye!")
    elif(question == 'y' or question == 'Y'):
        gameplay()
    return
#checks the guess and provides a code
def checkGuess(guess, secret):
    clue = []
    secretCopy = secret.copy()
    correct = [2,2,2,2]
    for i in range(0,4):
        if(guess[i] == secret[i]):
            clue.append(2)
            guess[i] = "Guessed"
            secretCopy[i] = -2
    for i in range (0,4):
        if(guess[i] in secretCopy):
            clue.append(1)
            secretCopy.remove(guess[i])
    if(clue == correct):
        return -1
    clue.sort()
    return clue
#makes the code using random numbers and the list of colors
def makeCode():
    ALL_COLORS = ['red','orange','yellow','green','blue','purple']
    secret = []
    for i in range (0,4):
        temp = random.randint(0,5)
        secret.append(ALL_COLORS[temp])
    return secret

#asks the user for inputs until a proper guess is provided
def makeGuess():
    ALL_COLORS = ['red','orange','yellow','green','blue','purple']
    guess = []
    print("-----------------------------")
    print("Make a guess of four colors:")
    print("0  -  red")
    print("1  -  orange")
    print("2  -  yellow")
    print("3  -  green")
    print("4  -  blue")
    print("5  -  purple")
    print("-----------------------------")
    for i in range (0,4):
        good = False
        while good == False:
            temp = (input("Guess color: "))
            try:
                int(temp)
                temp = int(temp)
                if(int(temp) > 5 or int(temp) < 0):
                    print("Invalid guess, try again:")
                else:
                    good = True
                    guess.append(ALL_COLORS[temp])
            except ValueError:
                print("Invalid number, try again:")
    print("-----------------------------")
    print("Your guess is:")
    print(guess, '\n')
    return guess
#plays the game, calls all other functions and such, also provides the guesses left
def gameplay():
    secret = makeCode()
    i = 9
    print("The secret code has been chosen. You have 10 tries to guess the code.", '\n')
    while i >= 0:
        guess = makeGuess()
        clue = checkGuess(guess, secret)
        if(clue == -1):
            print("Correct! You finished in ", 10-i, " guesses", '\n')
            reset()
            return
        print("Your clue is: ", clue, '\n')
        if(i == 0):
            print("No more guesses, the hidden colors were: ", "\n")
            print(secret, "\n")
        else:
            print("You have ", i, " guesses left")
        i -= 1
    
    reset()
    return
#main function
def main(seedValue):
    random.seed(seedValue)
    gameplay()
    return
