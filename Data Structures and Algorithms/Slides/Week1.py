'''
Data: A sequence of symbols that can be translated into information through an act of interpretation 
Metadata: Context that allows us to translate data in information.

Information: Data after it has been interpreted.
Knowledge: Theoretical/Practical understanding of a subject.
Wisdom: The ability to make good judgements based on knowledge and experience.

For example, given a bunch of morse code symbols (Data), we can translate it into information by using the morse code table (Metadata).
'''

'''
Structure:
Organization of a collection of related components that forms a whole, so it can support a certain function.

Data structure:
Collection of data values, the relationships between these data values, and the functions that can be applied to these data values.
'''

'''
O notations:

O(1): Constant time, whereby the time taken to execute the function is independent of the size of the input
O(log n): Logarithmic time, whereby the time taken to execute the function is proportional to the logarithm of the size of the input
O(n): Linear time, whereby the time taken to execute the function is proportional to the size of the input
O(n log n): Linearithmic time, whereby the time taken to execute the function is proportional to the product of the size of the input and the logarithm of the size of the input
O(n^2): Quadratic time, whereby the time taken to execute the function is proportional to the square of the size of the input
'''

'''
Array:
Data structure that stores data in a continuous block of computer memory
    Advantages:
        - allow random access (e.g. fast access)
        - easy to copy, and
        - use less computer memory
    Disadvantages:
        - fixed size
        - slow insertion and deletion
        - slow search
Would typically store homogenous data, whereby all units of data have the same data size

Linked list:
Stores data in one continuous piece of computer memory. However it breaks data down into nodes. Nodes are units of storage that store data, as
well as a reference to a memory address from another node.
    Advantages:
        - flexible to add new items dynamically, making it expandable
    Disadvantages:
        - access to data in a linked data structure may not be as fast as in arrays.
Would typically store heterogenous data, whereby all units of data have different data sizes

Queue:
Data structure that stores data in a first-in-first-out (FIFO) manner. The behavior of a queue is specified by a set of only 3 functions
namely, enqueue, dequeue and get.
    Advantages:
        - useful in situations where you want to process data in the order that they are received
    Disadvantages:
        - not useful in situations where you want to process data in a different order

Stack:
Data structure that stores data in a first-in-last-out (FILO) manner. The behavior of a stack is specified by a set of only 3 functions
namely, push, pop and get.
    Advantages:
        - useful in situations where you want to process data in the reverse order that they are received
    Disadvantages:
        - not useful in situations where you want to process data in a different order
'''

'''
Algorithm:
Series of steps to solve a specific problem

Types of Algorithms:
    Brute Force:
        Tries all candidate solutions until it finds a solution that works
        Properties:
            - Easy to implement
            - Not efficient, especially in large datasets
    Divide and Conquer:
        Breaks down a problem into smaller sub-problems which are easier to solve
        Properties:
            - More efficient
            - Relies on recursive coding
    Backtracking:
        Trys to find a solution incrementally by trying partial solutions and then abandoning them if they are not suitable
        Properties:
            - Only useful in certain problem domains
            - More efficient than brute force
            - Harder to implement 
            - Relies on recursion and tree search
'''

'''
Encapsulation:
Form of information hiding whereby the data can only be accessed indirectly through the access functions

Abstact Data Type (ADT):
Data-structure in terms of what functions we can perform with it, but does not reveal how these functions are implemented internally.

Stack:
Linear data structure whereby you can only work on the top (like a stack of plates). The behavior of a stack is specified by a set of only 3 functions 
namely, push, pop and get.
'''

'''
data data information metadata
'''