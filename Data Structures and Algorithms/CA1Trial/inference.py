import os
from history import History

class inference:
    def __init__(self, textFile, refFile, folder = None):
        self.__textFile = textFile
        self.__refFile = refFile
        self.__highestFreqUni = None
        self.__folder = folder
        self.__history = History()
    
    def unicodeSearch(self):
        '''
        -Find highest frequency letter from input file
        -Convert highest frequency letter to E using ord/chr
        -Calculate key using ord/chr
        -Return key
        '''
        with open(self.__refFile, "r") as file:
            freqtext = file.read()

        pairs = [line.split(',') for line in freqtext.split('\n')]

        # Convert to a dictionary by taking the letter on top as the key, and the number below as the value
        result = {pair[0]: float(pair[1]) for pair in pairs}
        sorted_dict = dict(sorted(result.items(), key = lambda x: x[1], reverse=True))
        # print(sorted_dict)
        self.__highestFreqUni = ord(list(sorted_dict.keys())[0])

    def inferKey(self, **kwargs):
        from fileAnalysis import LinkedList
        from fileCypher import FileCaesarCipher

        # Sort dict of letters using linkedlist
        linkedList = LinkedList(self.__textFile)
        sorted_letters = dict(linkedList.letterCount())
        # print(sorted_letters)
        if not sorted_letters:
            print("Error: No letters found in the file.")
            return None  # Return None if no letters found in the file

        # Get the ord of the most frequent letter
        highestOccurrence = int(ord(list(sorted_letters.keys())[0]))
        return highestOccurrence - self.__highestFreqUni

        


#Testing
# inference_instance = inference("ToDecrypt.txt", "englishtext.txt")
# inference_instance.unicodeSearch()
# inference_instance.inferKey()

# inference_instance.writefile("output.txt")