from collections import Counter
import matplotlib.pyplot as plt

class Node:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
        self.next = None

class LinkedList:
    def __init__(self, filename):
        self.head = None
        self.__filename = filename

    def insert(self, letter, frequency):
        new_node = Node(letter, frequency)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        current = self.head
        while current:
            print(f"{current.letter}: {current.frequency}")
            current = current.next
    
    def letterCount(self):
        with open(self.__filename, 'r') as file:
            text = file.read().upper()
        '''    
        Filter all punctuation, make all text uppercase to keep consistency    
        Next, sort letters in descending order of frequency. If same frequency, sort by alphabetical order(in this case x[0] in the nodes, while the numerical vals are x[1])
        Initialiose Linked list, sort by frequency, then by alphabetical order
        After sorting,  
        For plotting, I can use inheritance to inherit the linked list class and add a plot method to it.
        '''
        #Sort letters
        totalLetters = Counter(filter(str.isalpha, text))
        sorted_letters = sorted(totalLetters.items(), key=lambda x: (x[1], x[0]))
        # Check if letter frequency is correctly displayed/sorted
        for letter, frequency in sorted_letters:
            self.insert(letter, frequency)
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def plotGraph(self):
        frequencies = {node.letter: ((node.frequency100)*26) for node in self}
        print(frequencies)

        max_frequency = max(frequencies.values())
        print(max_frequency)

        for i in range(max_frequency, 0, -1):
            row = ''
            for char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
                count = frequencies.get(char, 0)
                if count >= i:
                    row += '* '
                else:
                    row += '  '
            print(row)

        # print('|')
        print('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
