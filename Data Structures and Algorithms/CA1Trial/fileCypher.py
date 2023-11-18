from CaesarCipher import CaesarCipher
import os

class FileValidationError(Exception):
    pass

class FileCaesarCipher(CaesarCipher):
    def __init__(self, shift, file_path, choice):
        self.__file_path = file_path
        with open(file_path, 'r') as file:
            text = file.read()
        super().__init__(shift, text)
        self.__choice = choice

    def get_full_path(self, file_path):
        # Combine the provided file path with the current working directory
        return os.path.join(os.getcwd(), file_path)

    def getFile(self):
        full_path = self.get_full_path(self.__file_path)
        try:
            with open(full_path, 'r') as file:
                data = file.read()
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f'File {full_path} not found')

    def encrypt_file(self, shift):
        self.__shift = shift
        data = self.getFile()
        encrypted_text = self.CaesarCrypt(self.__choice, self.__shift, data)
        # with open(self.__file_path, "w") as file:
        #     file.write(encrypted_text)
        return encrypted_text

    def decrypt_file(self, shift):
        self.__shift = shift
        data = self.getFile()
        decrypted_text = self.CaesarCrypt(self.__choice, self.__shift, data)
        # with open(self.__file_path, "w") as file:
        #     file.write(decrypted_text)
        return decrypted_text
