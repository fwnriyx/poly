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
    def user_choice():
        input("Press enter key, to continue....\n")
        choice = input(f"Please select your choice: (1,2,3,4,5,6,7,8)")

        return choice


    def menu(self): 
        self.print_self()
        while True:
            menu = ['Encrypt/Decrypt Message', 'Encrypt/Decrypt File', 'Analysze letter frequency distribution', 'Infer caesar cipher key from file Text', 
                    'Analyze, and sort encrypted files', 'Extra Option One','Extra Option Two', 'Exit']
            user_choice = int(self.user_choice())
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
            elif user_choice == 9:
                self.__choice9()
            elif user_choice == 10:
                self.__choice10()
                return
    def __choice1(self):
        from CaesarCipher import textEncoder

