import os

class inference:
    def __init__(self, textFile, refFile, folder="EncryptedFiles"):
        self.__textFile = textFile
        self.__refFile = refFile
        self.__highestFreqUni = None
        self.__folder = folder
    
    def unicodeSearch(self):
        '''
        -Find highest frequency letter from input file
        -Convert highest frequency letter to E using ord/chr
        -Calculate key using ord/chr
        -Return key
        '''
        with open((os.path.join(self.__folder, self.__refFile)), "r") as file:
            freqtext = file.read()

        pairs = [line.split(',') for line in freqtext.split('\n')]

        # Convert to a dictionary by taking the letter on top as the key, and the number below as the value
        result = {pair[0]: float(pair[1]) for pair in pairs}
        sorted_dict = dict(sorted(result.items(), key = lambda x: x[1], reverse=True))
        # print(sorted_dict)
        self.__highestFreqUni = ord(list(sorted_dict.keys())[0])
    
    def inferKey(self, output_folder = "DecryptedFiles"):
        from fileAnalysis import LinkedList
        from fileCypher import FileCaesarCipher
        '''
        Using the most frequent unicode in the reference file, we convert the most reoccuring
        letter in our text file to the most frequent unicode in the reference file, which is E.
        We then use the difference between the unicode of E and the unicode of the most frequent
        letter in our text file to infer the key.

        After that, we use the decrypt function from caesar cipher to decrypt the file and write it into
        the output file.
        '''
        #Sort dict of letters using linkedlist
        self.__folder = "EncryptedFiles"
        linkedList = LinkedList(self.__textFile)
        sorted_letters = dict(linkedList.letterCount())
        #Get the ord of most frequent letter
        # print(sorted_letters)
        highestOccurence = int(ord(list(sorted_letters.keys())[0]))
        # print(type(self.__highestFreqUni))


        choice = input(f"The inferred caesar cipher is: {highestOccurence - self.__highestFreqUni}.\nWould you like to decrypt the file? (Y/N): ").lower()
        if choice == 'y':
            # Instantiate FileCaesarCipher
            file_cipher = FileCaesarCipher(highestOccurence - self.__highestFreqUni, os.path.join(self.__folder, self.__textFile), "D")
            decrypted_text, _ = file_cipher.decrypt_file(highestOccurence - self.__highestFreqUni)
    
            # Use the decrypted_text as needed
            outputFile = input("Please enter an output file: ")
            output_path = os.path.join(output_folder, outputFile)

            with open(output_path, "w") as f:
                f.write(decrypted_text)

            print("File decrypted successfully!")

        


#Testing
# inference_instance = inference("StarTwinkle.txt", "englishtext.txt", "EncryptedFiles")
# inference_instance.unicodeSearch()
# inference_instance.inferKey()

# inference_instance.writefile("output.txt")