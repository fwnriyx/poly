'''
Name:       Liang Zheng Kai Lucas & Muhammad Fitri Amir Bin Abdullah
Admin No.:  2222770
Class:      DAAA2B06

DSAA Assignment 2
'''

import re

# Hash Table
class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.buckets = [None] * size

    # Pass the current size as an argument to hashFunction
    def hashFunction(self, key, current_size):
        if key == 0:
            return 0
        return sum(ord(char) for char in key) % current_size

    def rehashFunction(self, oldHash):
        return (oldHash + 1) % self.size

    # def rehashFunction(self, oldHash, attempt):
    #     return (oldHash + attempt) % self.size

    def _resize_and_rehash(self):
        new_size = self.size * 2 
        new_keys = [None] * new_size
        new_buckets = [None] * new_size

        # Use a while loop to ensure all non-empty buckets are processed
        index = 0
        while index < self.size:
            if self.keys[index] is not None: # a key exists
                # new_index = self.hashFunction(self.keys[index], self.size)  # Use the new size for hashing
                new_index = self.hashFunction(self.keys[index], new_size) #get new index for this key using the new size
                condition = True
                while condition:
                    # use bucket if empty
                    if new_buckets[new_index] == None:
                        # set the bucket by indexing the old bucket 
                        new_buckets[new_index] = self.buckets[index] 
                        condition = False # break the loop when bucket is found
                    else: # look for another available bucket
                        new_index = self.rehashFunction(new_index)
                        condition = True # run the loop again
                new_keys[new_index] = self.keys[index]
                new_buckets[new_index] = self.buckets[index]
            index += 1

        # Update the hash table 
        self.size = new_size  
        self.keys = new_keys
        self.buckets = new_buckets

    def __setitem__(self, key, value):
        index = self.hashFunction(key, self.size)
        startIndex = index
        while True:
            # Set new or replace existing key
            if self.keys[index % self.size] is None or self.keys[index % self.size] == key:
                self.buckets[index % self.size] = value
                self.keys[index % self.size] = key
                break
            else: 
                index = self.rehashFunction(index) # rehash and try to find empty bucket 
                if index == startIndex: # if there is no space, enter this condition
                    # Resize the hash table
                    # if sum(bucket is not None for bucket in self.buckets) >= self.size:
                        self._resize_and_rehash()
                        
                        # Recalculate the index using the new size
                        index = self.hashFunction(key, self.size)
                                                    
                        # insert the key and value
                        # there will definitely be space in this new hashtable
                        condition = True
                        while condition:
                            # if new resized hashtable bucket is empty use it
                            if self.buckets[index] == None: 
                                self.buckets[index] = value
                                self.keys[index] = key
                                condition = False # break loop when bucket found
                            else: #don't need to handle same key as handled above already
                                index = self.rehashFunction(index)
                                condition = True #continue loop/rehashing until bucket found
                        break

    def __getitem__(self, key):
        index = self.hashFunction(key, self.size)
        count = 0
        while True:
            if self.keys[index % self.size] == key:
                return self.buckets[index % self.size]
            else:
                index = self.rehashFunction(index)
                count += 1
                if count == self.size:
                    return None