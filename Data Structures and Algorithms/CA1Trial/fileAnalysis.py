import matplotlib.pyplot as plt
from collections import Counter

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
    
    def letterCount(self, filename):
        with open(self.__filename, 'r') as filename: 
            text = filename.read().upper()
        '''    
        Filter all punctuation, make all text uppercase to keep consistency    
        Next, sort letters in descending order of frequency. If same frequency, sort by alphabetical order(in this case x[0] in the nodes, while the numerical vals are x[1])
        Initialiose Linked list, sort by frequency, then by alphabetical order
        '''
        totalLetters = Counter(filter(str.isalpha, text))
        sorted_letters = sorted(totalLetters.items(), key=lambda x: (x[1], x[0]))
        linked_list = LinkedList()
        for letter, frequency in sorted_letters:
            linked_list.insert(letter, frequency)
    
        