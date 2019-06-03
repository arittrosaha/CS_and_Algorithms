# Queues - first in, first-out (FIFO)

# Queues libraries
    # s.append(e) - pushing at the end
    # q[0] - peeking at the front without popping
    # q.popleft() - will remove and return the first element

    

# Stacks - last in, first-out (LIFO)
    # linked list - pop and push are O(1)
    # arrays - pop and push are ammortized O(1)
    # peek - should return the last element without poping it
    # error handling - pop or peek should return None or raise error if its empty

# Stack libraries
    # s.append(e) - pushing at the end
    # s[-1] - peeking at the end without popping
    # s.pop() - will remove and return the last element
    # len(s) - 0 tests if the stack is empty

# s[-1] and s.pop() both raises Indexerror for empty list

# Stacks using arrays/list
class StackWithArrays:
    def __init__(self, given_stack=[]):
        self.stack = given_stack

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if len(self.stack):
            return None
        else:
            popped_element = self.stack.pop()
            return popped_element
    
    def peek(self):
        if len(self.stack):
            return None
        else:
            return self.stack[-1]
            

# ref -> https://stackoverflow.com/questions/67631/how-to-import-a-module-given-the-full-path?noredirect=1&lq=1
import importlib.util
spec = importlib.util.spec_from_file_location(
    "0", "/Users/arittrosaha/Dropbox/Education/Coding/CS and Algorithms/epi_study/7_linked_lists/0.py"
    )
zero = importlib.util.module_from_spec(spec)
spec.loader.exec_module(zero)
SinglyListNode = zero.SinglyListNode


class StackWithLL():
    def __init__(self, given_head=None):
        self.stack_head = given_head
    
    def push(self, new_head):
        if self.stack_head:
            new_head.next, self.stack_head = self.stack_head, new_head
        else:
            self.stack_head = new_head
    
    def pop(self):
        if self.stack_head:
            temp = self.stack_head
            self.stack_head = self.stack_head.next
            temp.next = None
            return temp.data
        else:
            return None
    
    def peek(self):
        if self.stack_head:
            return self.stack_head.data
        else:
            return None