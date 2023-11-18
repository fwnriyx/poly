import os
from os.path import exists,isfile

class CaesarCipher:
    def __init__(self, shift = None, text = None, result = ""):
        self.__shift = shift
        self.__text = text
        self.__result = result
    #Task 1a/2a - Encrypt Message From File/User Input
    #To do: Menu, EncDec Message and File
    #To do: Menu, EncDec Message and File
    '''
    From the example, the sentence is "The quick brown fox jumps over the lazy dog". When encrypted by -3,
    the result is "Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald". 
    When decrypted, the result is "The quick brown fox jumps over the lazy dog" and the shift is -3.
    This means that the given shift by the user is the shift used to encrypt the message, not the shift that the user wants to use to decrypt the message.
    '''
    # @staticmethod
    def CaesarCrypt(self, choice, shift, text):
        self.__shift = shift
        self.__text = text
        if choice == "D":
            self.__shift *= -1
        elif choice != "E" and choice != "D":
            raise ValueError(f'Invalid input')
        for i in range(len(self.__text)):
            char = self.__text[i]
            if (char.isupper()):
                '''
                For encoding:
                Steps for positive shift: 
                    - conver character to utf
                    - add shift 
                    - deduct 64 to find position in alphabet 
                    - mod 26 to find which alphabet 
                    - add 65 to find utf of alphabet
                '''
                #To encrypt text, shift by value and add to result mod 26 so that it doesnt go over 26 (for example Z +1 needs to go to A, not 27)
                if(((ord(char) + self.__shift - ord("A")) % 26) + ord("A")) < 0:
                    #A = 65, negative shift 1, Need it to go to Z, start from the back (for back shifts that turn utf < 65 aka alphabet < 0) 
                    self.__result += chr(((ord(char) + self.__shift - ord("A")) % 26) + ord("Z"))
                else:
                    #Z = 90, positive shift 1, Need it to go to A, starting from the front (forward shift cases and back shift where the utf still > 65) 
                    self.__result += chr(((ord(char) + self.__shift - ord("A")) % 26) + ord("A"))
            elif (char.islower()):
                if(((ord(char) + self.__shift - 97) % 26) + 97) < 0:
                    self.__result += chr(((ord(char) + self.__shift - ord("a")) % 26) + ord("z"))
                else:
                    self.__result += chr(((ord(char) + self.__shift - ord("a")) % 26) + ord("a"))
            else:
                self.__result += char  
        # print(f"Plaintext:\n {self.__text}\n Encrypted text:\n {self.__result}")
        return self.__result, self.__text

"""
Using inheritance (CaesarCrypt as parent and next class as child), I would like to replicate the same function 
as the parent class but with the file as the input instead of user input.
"""