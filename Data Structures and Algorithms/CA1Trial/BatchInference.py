import os
from inference import inference
from history import History

class BatchInference(inference):
    def __init__(self, ref_file="englishtext.txt"):
        super().__init__("", ref_file)
        self.__decryption_info = []
        self.__history = History()

    def batch_process_files(self):
        folder_path = input("Please enter the folder name: ")

        # Check if the folder exists
        if not os.path.exists(folder_path):
            print(f"The folder '{folder_path}' does not exist. Exiting batch processing.")
            return

        # Get a list of encrypted files in the folder
        encrypted_files = [f for f in os.listdir(folder_path) if f.endswith(".txt")]

        # Process each encrypted file
        for index, encrypted_file in enumerate(encrypted_files, start=1):
            print(f"\nDecrypting: {encrypted_file} with key: ", end="")
            
            current_file_path = os.path.join(folder_path, encrypted_file)
            self._inference__textFile = current_file_path
            self.unicodeSearch()

            with open(current_file_path, "r") as file:
                original_text = file.read()
            # Capture decryption information
            decryption_info = self.inferKey()

            from fileCypher import FileCaesarCipher
            filecipher_instance = FileCaesarCipher(decryption_info, current_file_path, "D")
            decrypted_text= filecipher_instance.decrypt_file(decryption_info)

            decrypted_file_path = os.path.join(folder_path, f"file{index}.txt")
            with open(decrypted_file_path, "w") as f:
                f.write(decrypted_text)
            # decrypted_file = f"file{index}.txt"


            decrypted_file = f"file{index}.txt"
            self.__decryption_info.append((decrypted_file, decryption_info))

            self.__history.add_entry(original_text, 'Decrypt File', decrypted_text)

            print(f"{decryption_info} as: {decrypted_file}")

        # Create a log file
        self.create_log_file(folder_path)

    def create_log_file(self, folder_path):
        log_file_path = os.path.join(folder_path, "log.txt")

        with open(log_file_path, "w") as log_file:
            # Filter out entries with None keys before sorting
            valid_entries = [(decrypted_file, key) for decrypted_file, key in self.__decryption_info if key is not None]

            # Sort the valid entries
            sorted_entries = sorted(valid_entries, key=lambda x: x[1])

            for index, (decrypted_file, key) in enumerate(sorted_entries, start=1):
                log_file.write(f"Decrypting: {decrypted_file} with key: {key} as: file{index}.txt\n")

        print(f"Log file created: {log_file_path}")

# Testing batch processing
# batch_instance = BatchInference()
# batch_instance.batch_process_files()
