from collections import Counter
import math
import os
#REPLACE COUNTER CHECK IF CAN USE MATH


class Node:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
        self.next = None

class LinkedList():
    def __init__(self, filename):
        self.head = None
        self.__filename = filename
        self.__text = ""
        self.__sorted_letters = []

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
            self.__text = file.read().upper()
        '''    
        Filter all punctuation, make all text uppercase to keep consistency    
        Next, sort letters in descending order of frequency. If same frequency, sort by alphabetical order(in this case x[0] in the nodes, while the numerical vals are x[1])
        Initialiose Linked list, sort by frequency, then by alphabetical order
        After sorting,  
        For plotting, I can use inheritance to inherit the linked list class and add a plot method to it.
        '''
        #Sort letters
        letter_counts = {}
        #letter_counts = {chr(i): 0 for i in range(ord('A'), ord('Z') + 1)}
        for char in self.__text:
            if char.isalpha():
                char = char.upper()  # Convert to uppercase to make it case-insensitive
                letter_counts[char] = letter_counts.get(char, 0) + 1
        sorted_letters = sorted(letter_counts.items(), key=lambda x: (x[1], x[0]))
        # Check if letter frequency is correctly displayed/sorted
        for letter, frequency in sorted_letters:
            self.insert(letter, frequency)
        self.__sorted_letters = sorted_letters
        return sorted_letters
    
    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

    def sortLetters(self):
        if not self.__sorted_letters:
            self.letterCount()
            return self.__sorted_letters
        letter_counts = {}
        for char in self.__text:
            if char.isalpha():
                char = char.upper()
                letter_counts[char] = letter_counts.get(char, 0) + 1
        #change
        sorted_letters = sorted(letter_counts.items(), key=lambda x: (x[1], x[0]))
        for letter, frequency in sorted_letters:
            self.insert(letter, frequency)
        self.__sorted_letters = sorted_letters
        return sorted_letters

    def plotGraph(self):
        if not self.__sorted_letters:
            self.sortLetters()
        sorted_letters = self.__sorted_letters

        fullAlphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

        relative_frequencies = {node.letter: round(((node.frequency/100)*26), 2) for node in self}
        # print(relative_frequencies)
        lettercount = sum(node.frequency for node in self)

        #Divide by total number of letters in the text
        frequencies = {node.letter: round(((node.frequency/lettercount)*100), 2) for node in self}
        max_frequency = max(relative_frequencies.values())
        sorted_frequencies = sorted(frequencies.items(), key=lambda x: (x[1],x[0]))

        #I need to drop the letters if they are on the same level as any asterisks, so i can plot them later on
        #Do this by using ord() to get the ascii value of the letter, and then subtracting 65 (ascii value of A) 
        # + 1 because we want to include the letter itself
        '''
        Let's say max_frequency is 3.5. If you use math.ceil(3.5), it becomes 4. So, ord('Z') - 4 gives you the distance from 'Z' to the letter right above the asterisks, 
        but it doesn't include that letter itself. Hence, you add 1 to include that letter.
        '''
        totalLetters = ord('Z') - math.ceil(max_frequency) + 2
        final_letters = ""
        for i in range(ord('A'), totalLetters):
            final_letters += chr(i)  
        for letter in final_letters:
            count = frequencies.get(letter, 0)
            if letter == 'K':
                print(' ' * 52 + f'| {letter}- {count:.2f}%   Lowest 5 FREQ')
            elif letter == 'L':
                print(' ' * 52 + f'| {letter}- {count:.2f}%   -----------')
            elif letter == 'M':
                print(' ' * 52 + f'| {letter}- {count:.2f}%   | {sorted_letters[0][0]}: {frequencies[sorted_letters[0][0]]}%')
            elif letter == 'N':
                print(' ' * 52 + f'| {letter}- {count:.2f}%   | {sorted_letters[1][0]}: {frequencies[sorted_letters[1][0]]}%')
            elif letter == 'O':
                print(' ' * 52 + f'| {letter}- {count:.2f}%  | {sorted_letters[2][0]}: {frequencies[sorted_letters[2][0]]}%')
            elif letter == 'P':
                print(' ' * 52 + f'| {letter}- {count:.2f}%   | {sorted_letters[3][0]}: {frequencies[sorted_letters[3][0]]}%')
            elif letter == 'Q':
                print(' ' * 52 + f'| {letter}- {count:.2f}%   | {sorted_letters[4][0]}: {frequencies[sorted_letters[4][0]]}%')
                continue
            else:
                print(' ' * 52 + f'| {letter}- {count:.2f}%')
        #Get remaining letters that were removed as they were in the same line as asterisks
        final_letters = fullAlphabet.replace(final_letters, '')
        for i in range(math.ceil(max_frequency), 0, -1):
            row = ''
            for char in fullAlphabet:
                count = relative_frequencies.get(char, 0)
                r2 = math.ceil(count)
                if r2 >= i:
                    row += '* '
                else:
                    row += '  '
            '''
            Now, I need to get the final letters that were removed from the previous loop, and print them on the same line as the asterisks
            I can use indexing to index the letters from final_letters, and then use the index to get the frequency from frequencies
            final_letters[i - 1]
            '''
            # count = frequencies.get(final_letters[::-1][i - 1], 0)
            # row += f'| {final_letters[::-1][i - 1]}- {count:.2f}%'
            print(row)
            
            '''
            Because we are only left with the letters that are on the same level as asterisks, we can just loop through the letters and get their frequency
            '''
            
        print('─' * 52 + '')
        print('A B C D E F G H I J K L M N O P Q R S T U V W X Y Z')
                    

#Testing
# linkedList = LinkedList("TwinkleStar.txt")
# sorted_letters = dict(linkedList.sortLetters())
# linkedList.plotGraph()
