import os

class CaesarCipher:
    def __init__(self, shift,text):
        self.__shift = shift
        self.__text = text
        self.__result = ""

    #Task 1a/2a - Encrypt Message From File/User Input
    '''
    From the example, the sentence is "The quick brown fox jumps over the lazy dog". When encrypted by -3,
    the result is "Qeb nrfzh yoltk clu grjmp lsbo qeb ixwv ald". 
    When decrypted, the result is "The quick brown fox jumps over the lazy dog" and the shift is -3.
    This means that the given shift by the user is the shift used to encrypt the message, not the shift that the user wants to use to decrypt the message.
    '''
    def textEncoder(self):
        for i in range(len(self.__text)):
            char = self.__text[i]
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
                if(((ord(char) + self.__shift - ord("A")) % 26) + ord("A")) < 0:
                    #A = 65, negative shift 1, Need it to go to Z, start from the back (for back shifts that turn utf < 65 aka alphabet < 0) 
                    result += chr(((ord(char) + self.__shift - ord("A")) % 26) + ord("Z"))
                else:
                    #Z = 90, positive shift 1, Need it to go to A, starting from the front (forward shift cases and back shift where the utf still > 65) 
                    result += chr(((ord(char) + self.__shift - ord("A")) % 26) + ord("A"))
            elif (char.islower()):
                if(((ord(char) + self.__shift - 97) % 26) + 97) < 0:
                    result += chr(((ord(char) + self.__shift - ord("a")) % 26) + ord("z"))
                else:
                    result += chr(((ord(char) + self.__shift - ord("a")) % 26) + ord("a"))
            else:
                result += char  
        return result

class FileCaesarCipher(CaesarCipher):
    def __init__(self, shift, file_path):
        with open(file_path, 'r') as file:
            text = file.read()
        super().__init__(shift, text)
        self.__file_path = file_path

    def file_validation(self):
        if not os.path.isfile(self.__file_path):
            raise FileNotFoundError(f'File {self.__file_path} not found')

    def encrypt_file(self):
        encrypted_text = self.encrypt()
        with open(self.__file_path, 'w') as file:
            file.write(encrypted_text)

    def decrypt_file(self):
        decrypted_text = self.decrypt()
        with open(self.__file_path, 'w') as file:
            file.write(decrypted_text)