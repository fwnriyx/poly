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

    