import random
guessedNumber = []
def RandomNum(n):
    return random.randint(1,n)
def GuessRandomly(maxNum):
    myGuess = None
    noOfGuesses = 0
    while(True):
        myGuess = RandomNum(maxNum)
        noOfGuesses+=1
        print(f'My guess is: {myGuess}')
        guessedCorrectly= input("Correct 'y' or 'n'?") == "y"
        if guessedCorrectly:
            print(f'Wonderful it took me {noOfGuesses} attempts to guess that you had the number {myGuess} in mind!')
            break
# Main programme
maxNum = int( input('Enter the range: '))
input(f'Think of a random number between 1 and {maxNum} and press enter once done!')
GuessRandomly(maxNum)