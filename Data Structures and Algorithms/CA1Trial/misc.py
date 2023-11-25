'''
Name: Muhammad Fitri Amir bin Abdullah
Class: DAAA/FT/2A/06
Admin no: 2222811
'''

"""
Why use @static methods?
Static methods are used to group functions which have some logical connection with a class to the class. 
"""

'''
Fixes needed:
    - Relative pathing
    - Formatting answers
    - Option 5 (needs inheritance)
    - 2 extra feature ideas
Unfortunately I was unable to complete the 2 extra feature ideas due to time constraints.
'''
import os
from history import History

class misc:
    def __init__(self):
        self.history = History()
        pass

    def boxbox():
        text = """ST1507 DSAA: Welcome to:
        ~Caesar Cipher Encrypted Message Analyzer~
        ------------------------------------------

        - Done by Fitri Amir (P2222811)
        - Class DAAA/FT/2A/06
        """
        lines = text.split('\n')
        max_line_length = max(len(line) for line in lines) 
        box_width = max_line_length + 4 
        
        print('*' * box_width)
        
        for line in lines:
            padding = (max_line_length - len(line)) // 2
            print('* ' + ' ' * padding + line + ' ' * (max_line_length - len(line) - padding) + ' *')
        
        print('*' * box_width)
    
    @staticmethod
    def user_choice(menu):
        input("Press enter key, to continue....\n")
        choices = list(f'\t{idx+1}: {option}' for idx, option in enumerate(menu))
        message = f"Please select your choice: \n {str(tuple(range(1,len(menu)+1))).replace(' ', '') }\n" + '\n'.join(choices) + '\nEnter choice:'
        #Validate user input
        try:
            choice = int(input(message))
            if choice not in range(1, len(menu)+1):
                raise ValueError
        except ValueError:
            print(f'Invalid input')
            return misc.user_choice(menu)
        return message, choice

    def menu(self): 
        while True:
            menu = ['Encrypt/Decrypt Message', 'Encrypt/Decrypt File', 'Analysze letter frequency distribution', 'Infer caesar cipher key from file Text', 
                    'Analyze, and sort encrypted files', 'Check Encryption and Decryption history','Extra Option Two', 'Exit']
            message, user_choice = misc.user_choice(menu)
            if user_choice == 1:
                self.__choice1()
            elif user_choice == 2:
                self.__choice2()
            elif user_choice == 3:
                self.__choice3()
            elif user_choice == 4:
                self.__choice4()
            elif user_choice ==5:
                self.__choice5()
            elif user_choice == 6:
                self.__choice6()
            elif user_choice == 7:
                self.__choice7()
            elif user_choice == 8:
                self.__choice8()
                return
            
    def __choice1(self):
        from CaesarCipher import CaesarCipher  # Import the CaesarCipher class
        choice = input(f'Enter "E" for encryption, "D" for decryption: ').upper()
        if choice != "E" and choice != "D":
            print(f'Invalid input')
            #Dont break the program if user enters invalid input, redirect to menu
            pass
        else:
            try:
                shift = int(input(f"Enter the cipher key: "))
                text = input(f"Please type text that you want to encrypt: ")
                caesar_cipher = CaesarCipher()  # Create an instance of the CaesarCipher class
                result, text = caesar_cipher.CaesarCrypt(choice, shift, text)
                print(f"Plaintext:  {text}\nEncrypted text: {result}")
                if choice == "E":
                    choice = "Encrypt"
                elif choice == "D":
                    choice = "Decrypt"
                self.history.add_entry(text, choice, result)
            except ValueError:
                print("Invalid input. Please enter a valid integer for the cipher key.")

    def __choice2(self):
        from fileCypher import FileCaesarCipher
        choice = input(f'Enter "E" for encryption, "D" for decryption: ').upper()
        if choice != "E" and choice != "D":
            print(f'Invalid input')
            pass
        else:
            try:
                shift = int(input(f"Enter the cipher key: "))
                file_path = input("Enter the file path: ")
                file_cipher = FileCaesarCipher(shift, file_path, choice)
                if choice == "E":
                    choice = "Encrypt"
                    file_cipher.encrypt_file(shift)
                    print("File encrypted successfully!")
                elif choice == "D":
                    choice = "Decrypt"
                    file_cipher.decrypt_file(shift)
                    print("File decrypted successfully!")
                else:
                    print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")
                self.history.add_entry(file_path, choice, file_cipher)
            except ValueError:
                print("Invalid input. Please enter a valid integer for the cipher key.")

    def __choice3(self):
        from fileAnalysis import LinkedList
        filename = input("Enter the file path: ")
        try:
            letter_freq = LinkedList(filename)
            letter_freq.letterCount()
            letter_freq.plotGraph()
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")
        return self
    
    def __choice4(self):
        textFile = input("Please enter the file to analyze: ")
        refFile = input("Please enter the reference frequencies file: ") 
        try:
            from inference import inference
            inference_instance = inference(textFile, refFile)
            inference_instance.unicodeSearch()
            key = inference_instance.inferKey()
            if key is not None:
                choice = input(f"The inferred caesar cipher is: {key}.\nWould you like to decrypt the file using this key? (y/n): ").lower()
                if choice == "y":
                    from fileCypher import FileCaesarCipher
                    file_cipher = FileCaesarCipher(key, textFile, "D")
                    decrypted_text = file_cipher.decrypt_file(key)

                    outputFile = input("Please enter an output file: ")
                    print(decrypted_text)
                    with open(outputFile, "w") as f:
                        f.write(decrypted_text)
                    print("File decrypted successfully!")
                    self.history.add_entry(textFile, 'Decrypt', decrypted_text)
        except:
            print("Error: Invalid file path.")
        pass

    def __choice5(self):
        from BatchInference import BatchInference
        batch_instance = BatchInference()
        batch_instance.batch_process_files()
        pass

    def __choice6(self):
        self.history.display_history()
        pass

    def __choice8(self):
        print()
        print(f'Bye, thanks for using ST1507 DSAA: Caesar Cipher Encrypted Message Analyzer!')



# misc_instance = misc()
# #use box box
# misc.boxbox()
# misc_instance.menu()