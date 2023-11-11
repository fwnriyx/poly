'''
Name: Muhammad Fitri Amir bin Abdullah
Class: DAAA/FT/2A/06
Admin no: 2222811
'''

"""
Why use @static methods?
Static methods are used to group functions which have some logical connection with a class to the class. 
"""

class misc:
    def __init__(self):
        pass

    def boxbox(text):
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
                    'Analyze, and sort encrypted files', 'Extra Option One','Extra Option Two', 'Exit']
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
        choice = input(f'Enter "E" for encryption, "D" for decryption: ')
        shift = int(input(f"Enter the cipher key: \n"))
        text = input(f"Please type text that you want to encrypt: \n")
        caesar_cipher = CaesarCipher()  # Create an instance of the CaesarCipher class
        caesar_cipher.CaesarCrypt(choice, shift, text)

    def __choice2(self):
        from fileCypher import FileCaesarCipher
        choice = input(f'Enter "E" for encryption, "D" for decryption: ').upper()
        shift = int(input("Enter the cipher key: "))
        file_path = input("Enter the file path: ")
        file_cipher = FileCaesarCipher(shift, file_path, choice)
        
        if choice == "E":
            file_cipher.encrypt_file(shift)
            print("File encrypted successfully!")
        elif choice == "D":
            file_cipher.decrypt_file(shift)
            print("File decrypted successfully!")
        else:
            print("Invalid choice. Please enter 'E' for encryption or 'D' for decryption.")

    def __choice8(self):
        print()
        print(f'Bye, thanks for using my program!')
misc_instance = misc()
misc_instance.menu()


