# Implement a circular queue

# Prompt:
# A queue API using fixed sized array. 
# It should include constructor function
    # -> takes an argument - the initial capacity of the queue
    # -> enqueue, dequeue functions
    # -> function that returns the number of elements stored
    # -> implement dynamic resizing  

class Queue_EPI:
    SCALE_FACTOR = 2

    def __init__(self, initial_size):
        self._head = self._tail = self._number_of_elements = 0
        self._queue = [None] * initial_size
    
    def enqueue(self, element):  
        if self._number_of_elements == len(self._queue):
            self._queue = self._queue[self._head:] + self._queue[:self._head]
            # everything upto but not including the head + everything from head including the head
            self._queue += [None] * (len(self._queue) * self.SCALE_FACTOR - len(self._queue))
            # (number of elements * the scale) - one length of elements
        self._queue[self.tail] = element
        self._tail = (self._tail + 1) % len(self._entries)
        # modulo to make it circular
        self._number_of_elements += 1

    def dequeue(self):
        self._queue[self._head] = None
        self._head = (self._head + 1) % len(self._entries)
        self._number_of_elements -= 1
    
    def queue_length(self):
        return self.number_of_elements



    
    

        
     



