class History:
    def __init__(self):
        self.__history_list = []

    def add_entry(self, original, operation, result):
        entry = {
            'originalText': original,
            'cryptType': operation,
            'result': result
        }
        self.__history_list.append(entry)

    def display_history(self):
        if self.__history_list == []:
            print("\nHistory is empty.")
        else:
            print(f"\nHistory:")
            for entry in self.__history_list:
                if entry['cryptType'] == 'E':
                    print(f"{entry['cryptType']}ion of '{entry['originalText']}' to '{entry['result']}'")
                #   print(f"{entry['cryptType']}ion of '{entry['originalText']}' to '{entry['result']}'")
                elif entry['cryptType'] == 'D':
                    print(f"{entry['cryptType']}ecryption of '{entry['originalText']}' to '{entry['result']}'")