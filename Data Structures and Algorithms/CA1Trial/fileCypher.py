from CaesarCipher import CaesarCipher

class FileValidationError(Exception):
    pass

class FileCaesarCipher(CaesarCipher):
    def __init__(self, shift, file_path, choice):
        self.__file_path = file_path
        with open(file_path, 'r') as file:
            text = file.read()
        super().__init__(shift, text)
        self.__choice = choice
        # self._CaesarCipher__text = text  # Accessing private variable from the parent class
        

    def getFile(self):
        try:
            with open(self.__file_path, 'r') as file:
                data = file.read()
            return data
        except FileNotFoundError:
            raise FileNotFoundError(f'File {self.__file_path} not found')

    def encrypt_file(self, shift):
        self.__shift = shift
        data = self.getFile()
        encrypted_text = self.CaesarCrypt(self.__choice, self.__shift, data)
        # with open(self.__file_path, "w") as file:
        #     file.write(encrypted_text)

    def decrypt_file(self, shift):
        self.__shift = shift
        data = self.getFile()
        decrypted_text = self.CaesarCrypt(self.__choice, self.__shift, data)
        # with open(self.__file_path, "w") as file:
        #     file.write(decrypted_text)