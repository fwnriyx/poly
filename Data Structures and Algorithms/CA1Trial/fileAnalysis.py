class letterAnalysis:
    def __init__(self, letter, frequency):
        self.letter = letter
        self.frequency = frequency
        self.next = None
        

    def letterFreq(self):
        '''
        Make linked list, each node is a letter and the count of the letter
        Sort by highest frequency, get top 5 and print.
        '''
        