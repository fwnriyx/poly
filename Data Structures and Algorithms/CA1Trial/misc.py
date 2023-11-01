'''
Name: Muhammad Fitri Amir bin Abdullah
Class: DAAA/FT/2A/06
Admin no: 2222811
'''


class misc:

    def boxbox(text):
        lines = text.split('\n')
        max_line_length = max(len(line) for line in lines) 
        box_width = max_line_length + 4 
        
        print('*' * box_width)
        
        for line in lines:
            padding = (max_line_length - len(line)) // 2
            print('* ' + ' ' * padding + line + ' ' * (max_line_length - len(line) - padding) + ' *')
        
        print('*' * box_width)
    
    def numericalCheck(choice):
        try:
            int(choice)
            return True
        except ValueError:
            return False

    def menu(self): 
        self.print_self()
        while True:
            starting_choices = ['Encrypt/Decrypt Message', 'Encrypt/Decrypt File', 'Analysze letter frequency distribution', 'Infer caesar cipher key from file Text', 
                                'Analyze, and sort encrypted files', 'Extra Option One','Extra Option Two', 'Exit']
            user_choice = Utils.get_number_choice(arr_choices=starting_choices)
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