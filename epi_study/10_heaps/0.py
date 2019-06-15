# A heap is a complete binary tree
    # A complete binary tree's leaf level is all left skewed with no gaps in between and all nodes in previous level should have two children always

# Heap is also a priority queue
    # it's queue except every nodes has a priority and the node with the highest priority is the one that is first to be extracted

# Key functions:
    # insertions - log(n) because of shifting down
    # max/min lookup - O(1) because max/min is always at the root
    # deletion/extraction - log(n) ; you can only delete the root and then shifting up

# Max heap - the key at each node is at least as great as the keys stored at its children
# Min heap - the key at each node is at most as the keys stored at its children

import itertools
import heapq
def top_k(k, stream): # stream is an iterable object 
    # itertools.islice(iterable, stop) / itertools.islice(iterable, start, stop)
    # ref -> https://docs.python.org/2/library/itertools.html#itertools.islice
    # Why itertools.islice over normal slicing?
    # ref -> https://stackoverflow.com/questions/32172612/why-would-i-want-to-use-itertools-islice-instead-of-normal-list-slicing

    min_heap = [(len(s), s) for s in itertools.islice(stream, k)] # an list of tuples

    heapq.heapify(min_heap) # it seems it will heapify using value at the idx 0 if each element is an iterable themselves
    # heapq always creates a min heap. If max heap is needed, then flip the signs of the values

    for next_string in stream: # because stream is an iterable object, the iteration for this loop will start after where line 23 left off
        heapq.heappushpop(min_heap, (len(next_string), next_string))
    
    return [p[1] for p in heapq.nsmallest(k, min_heap)]

# heapq library: 
# ref -> https://docs.python.org/3/library/heapq.html
    # -> heapq.heapify(L)                             - transforms the elements in L into a heap in-place
    # -> heapq.nlargest(k, L) / heapq.nsmallest(k, L) - returns k largest / smallest list of elements in the iterable L which can be a heap
    # -> heapq.heappush(h, e)                         - pushes a new element, e on the heap, h
    # -> heapq.heappop(h)                             - pops the smallest element from the heap
    # -> heapq.heapushpop(h, a)                       - pushes on the heap and then pops and returns the smallest element
    # -> e = h[0]                                     - returns smallest element on the heap without popping it

class Heap:
    def __init__(self, iterable, type="min"):
        self.iterable = []
        self.type = type
        for idx, element in iterable:
            self.push(element, idx)
    
    def peek(self):
        return self.iterable[0]

    def push_pop(self, element, idx=None):
        self.push(element)
        return self.pop()

    def push(self, element, idx=None):
        if not idx:
            idx = len(self.iterable) - 1
        self.iterable.append(element)
        self.shift_up(idx)
    
    def shift_up(self, idx):
        if idx <= 0:
            return
        
        parent_idx = (idx - 2)/2 if idx % 2 == 0 else (idx-1)/2

        if self.iterable[idx] < self.iterable[parent_idx] and self.type == "min":
            self.iterable[idx], self.iterable[parent_idx] = self.iterable[parent_idx], self.iterable[idx]
            
        if self.iterable[idx] > self.iterable[parent_idx] and self.type == "max":
            self.iterable[idx], self.iterable[parent_idx] = self.iterable[parent_idx], self.iterable[idx]
        
        self.shift_up(parent_idx)

    def pop(self):
        self.iterable[0], self.iterable[-1] = self.iterable[-1], self.iterable[0]
        popped = self.iterable.pop()
        self.shift_down(0)
        return popped
    
    def shift_down(self, idx):
        if idx >= len(self.iterable):
            return
        
        left_child = self.iterable[2*idx+1]
        right_child = self.iterable[2*idx+2]

        if left_child and right_child:
            if self.type == "min":
                if left_child < right_child and left_child < self.iterable[idx]:
                    self.iterable[2*idx+1], self.iterable[idx] = self.iterable[idx], self.iterable[2*idx+1]
                    self.shift_down(2*idx+1)
                elif right_child < left_child and right_child < self.iterable[idx]:
                    self.iterable[2*idx+2], self.iterable[idx] = self.iterable[idx], self.iterable[2*idx+2]
                    self.shift_down(2*idx+2)
            elif self.type == "max":
                if left_child > right_child and left_child > self.iterable[idx]:
                    self.iterable[2*idx+1], self.iterable[idx] = self.iterable[idx], self.iterable[2*idx+1]
                    self.shift_down(2*idx+1)
                elif right_child > left_child and right_child > self.iterable[idx]:
                    self.iterable[2*idx+2], self.iterable[idx] = self.iterable[idx], self.iterable[2*idx+2]
                    self.shift_down(2*idx+2)
        elif left_child:
            if left_child < right_child and left_child < self.iterable[idx] and self.type == "min":
                self.iterable[2*idx+1], self.iterable[idx] = self.iterable[idx], self.iterable[2*idx+1]
                self.shift_down(2*idx+1)
            elif left_child > right_child and left_child > self.iterable[idx] and self.type == "max":
                self.iterable[2*idx+1], self.iterable[idx] = self.iterable[idx], self.iterable[2*idx+1]
                self.shift_down(2*idx+1)
            


