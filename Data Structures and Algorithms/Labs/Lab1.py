# Case Study: Number Guessing Game (slightly pseudocoded) Brute Force
'''
Its basically hard guessing all the numbers
'''
# import random
# def RandomNum(n):
#     return random.randint(1,n)
# def GuessRandomly(maxNum):
#     myGuess = None
#     noOfGuesses = 0
#     while(True):
#         myGuess = RandomNum(maxNum)
#         noOfGuesses+=1
#         print(f'My guess is: {myGuess}')
#         guessedCorrectly= input("Correct 'y' or 'n'?") == "y"
#         if guessedCorrectly:
#             print(f'Wonderful it took me {noOfGuesses}\
#                     attempts to guess that you had the number\
#                     {myGuess}in mind!')
#             break
# # Main programme
# maxNum = int( input('Enter the range: '))
# input(f'Think of a random number between 1\
#         and {maxNum} and press enter once done!')
# GuessRandomly(maxNum)

# Divide and conquer
'''
After each question Mary reduces the number of candidates by half therefore the cost equation will be:

Q(n) = log2 (n)
aka
log(n)
'''
#Pseudocode
'''
max = getMaxNumber()
johnsNumber = getJohnsNumber(1,max)
numberHasBeenGuessed = FALSE
noOfQuestions = 0
candidates = [1:max]
noOfCandidates = max

WHILE NOT numberHasBeenGuessed
    breakpointIndex = noOfCandidates/2
    breakpoint = candidates[breakpointIndex]

    IF askIfNumberIsSmallerThanBreakpoint
            (breakpoint,johnsNumber)
        candidates = leftSide(candidates,breakpoint)
    ELSE
        candidates = rightSide(candidates,breakpoint)

    noOfQuestions += 1
    IF length(candidates) == 1
        numberHasBeenGuessed = TRUE
printResult(noOfQuestions, candidates[0])
'''

#Task 1 Caesar Cipher

def textEncDec(text, shift):
    print(text)
    result = ""
    for i in range(len(text)):
        char = text[i]
        if (char.isupper()):
            '''
            Steps for positive shift: 
                - convert character to utf
                - add shift 
                - deduct 64 to find position in alphabet 
                - mod 26 to find which alphabet 
                - add 65 to find utf of alphabet
                - for small number -97 (use ord(a) if no hardcode)
            '''
            #To de/encrypt text, shift by value and add to result mod 26 so that it doesnt go over 26 (for example Z +1 needs to go to A, not 27)
            if(((ord(char) + shift - ord("A")) % 26) + ord("A")) < 0:
                #A = 65, negative shift 1, Need it to go to Z, start from the back (for back shifts that turn utf < 65 aka alphabet < 0) 
                result += chr(((ord(char) + shift - ord("A")) % 26) + ord("Z"))
            else:
                #Z = 90, positive shift 1, Need it to go to A, starting from the front (forward shift cases and back shift where the utf still > 65) 
                result += chr(((ord(char) + shift - ord("A")) % 26) + ord("A"))
        elif (char.islower()):
            if(((ord(char) + shift - 97) % 26) + 97) < 0:
                result += chr(((ord(char) + shift - ord("a")) % 26) + ord("z"))
            else:
                result += chr(((ord(char) + shift - ord("a")) % 26) + ord("a"))
        else:
            result += char
    return result

codedText = input("Enter text to encrypt: ")
shift = int(input("Enter shift value: "))
print("Encrypted text: ", textEncDec(codedText, shift))

#Task 2