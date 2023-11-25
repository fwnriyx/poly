from CaesarCipher import CaesarCipher
from history import History
import os

# class FileValidationError(Exception):
#     pass

# class FileCaesarCipher(CaesarCipher):
#     def __init__(self, shift, file_name, choice):
#         self.__file_name = file_name
#         with open(file_name, 'r') as file:
#             text = file.read()
#         super().__init__(shift, text)
#         self.__choice = choice
#         self.__history = History()

#     def getFile(self):
#         try:
#             with open(self.__file_name, 'r') as file:
#                 data = file.read()
#             return data
#         except FileNotFoundError:
#             raise FileNotFoundError(f'File {self.__file_name} not found')

#     def encrypt_file(self, shift):
#         self.__shift = shift
#         data = self.getFile()
#         encrypted_text = self.CaesarCrypt(self.__choice, self.__shift, data)

#         with open(f"file_encrypted.txt", "w") as file:
#             file.write(encrypted_text)
#         self.__history.add_entry(data, "Encrypt", encrypted_text)

#         return encrypted_text

#     def decrypt_file(self, shift):
#         self.__shift = shift
#         data = self.getFile()
#         decrypted_text = self.CaesarCrypt(self.__choice, self.__shift, data)
#         print(decrypted_text)
#         with open(f"file_decrypted.txt", "w") as file:
#             file.write(decrypted_text)
#         self.__history.add_entry(data, "Decrypt", decrypted_text)

#         return decrypted_text 
class FileCaesarCipher(CaesarCipher):
    def __init__(self, shift, file_name, choice):
        self.__file_name = file_name
        with open(file_name, 'r') as file:
            self.__text = file.read()
        super().__init__(shift, self.__text)
        self.__choice = choice
        self.__history = History()

    def encrypt_file(self, shift):
        self.__shift = shift
        encrypted_text, _ = self.CaesarCrypt(self.__choice, self.__shift, self.__text)

        with open(f"file_encrypted.txt", "w") as file:
            file.write(encrypted_text)
        # self.__history.add_entry(self.__text, "Encrypt", encrypted_text)

        return encrypted_text

    def decrypt_file(self, shift):
        self.__shift = shift
        data = self.__text
        decrypted_text, _ = self.CaesarCrypt(self.__choice, self.__shift, data)
        # Save the result to the file
        with open(f"file_decrypted.txt", "w") as file:
            file.write(decrypted_text)

        # self.__history.add_entry(data, "Decrypt", decrypted_text)
        # self.__history.add_entry(data, "Decrypt", decrypted_text[0])

        return decrypted_text  # Only return the decrypted text, not a tuple