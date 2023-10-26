file = None

def textEncDec(file, text, shift):
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