import random
import matplotlib.pyplot as plt
import numpy as np
from time import perf_counter

class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

    def insert(self, value):
        if value < self.value:
            if self.left is None:
                self.left = Node(value)
            else:
                self.left.insert(value)
        else:
            if self.right is None:
                self.right = Node(value)
            else:
                self.right.insert(value)
    
    # start of GPT code
    def find_min(self): 
        current = self
        while current.left != None:
            current = current.left
        return current.value
    # end of GPT code

x = []
y_insert = []
y_min = []
for n in range(10000,100000,1000):
    #create a random unsorted list
    unsorted = []
    for _ in range(n):
        unsorted.append(random.randint(0,n))


    #translate that to a binary tree insertion
    start = perf_counter()

    tree = Node(unsorted[0])
    for i in range(1,len(unsorted)):
        tree.insert(unsorted[i])

    end = perf_counter()

    x.append(n)
    y_insert.append(end-start)

    #find min
    start = perf_counter()
    for _ in range(10000):
        tree.find_min()
    end = perf_counter()
    y_min.append(end-start)



plt.plot(x, y_insert, label='Insertion')
plt.plot(x, y_min, label='Find Min')

# Add labels and a title for clarity
plt.xlabel("n")
plt.ylabel("time")
plt.title("Runtime plot")
plt.legend()

# Display the plot
plt.show()

