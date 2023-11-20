import os
from inference import inference

class BatchInference(inference):
    def __init__(self, folder="BatchDecrypt", refFile="englishtext.txt"):
        super().__init__("", refFile, folder)
        self.__file_list = []
        self.__decryption_info = []

    def get_file_list(self):
        return self.__file_list

    def batch_process_files(self):
        folder_path = input("Enter the folder name containing encrypted files: ")
        self.__folder = folder_path

        encrypted_files = [f for f in os.listdir(self.__folder) if f.endswith(".txt")]

        # Process each encrypted file
        for index, encrypted_file in enumerate(encrypted_files, start=1):
            print(f"\nProcessing file {index}: {encrypted_file}")

            # Set the path to the current encrypted file
            current_file_path = os.path.join(self.__folder, encrypted_file)
            
            # Access the __textFile attribute directly and set it
            self._inference__textFile = current_file_path

            self.unicodeSearch()

            # Capture decryption information
            decryption_info = self.inferKey(output_folder="DecryptedFiles")
            decrypted_file = f"file{index}.txt"
            self.__file_list.append(decrypted_file)
            self.__decryption_info.append(decryption_info)
    
        # Display decryption information in the console
        for info in self.__decryption_info:
            print(info)

        # Create a log file
        self.create_log_file()

    def create_log_file(self):
        log_file_path = os.path.join(self.__folder, "log.txt")
        with open(log_file_path, "w") as log_file:
            for index, (decrypted_file, key) in enumerate(zip(self.__file_list, self.__decryption_info), start=1):
                log_file.write(f"Decrypted file {index}: {decrypted_file} with key {key}\n")

        print(f"Log file created: {log_file_path}")

# Testing batch processing
batch_instance = BatchInference()
batch_instance.batch_process_files()
