# Linked List:
# -> is a data structure contains a sequence of nodes 
# -> each node contains an object and reference(s) to the next node and-or previous node
# -> head - the first node in the sequence
# -> tail - the last node in the sequence

# Two types of linked list:
# -> Singly linked list - each node only reference the next node
# -> Doubly linked list - each node references the next and the previous node

def print_list(ll):
    while ll:
        print(ll.data)
        ll = ll.next

class SinglyListNode:
    def __init__(self, data=0, next=None):
        self.data = data
        self.next = next

class SinglyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = self.__find_tail()
    
    def search_list(self, key): # Time: O(n)
        curr_node = self.head
        while curr_node and curr_node.data != key:
            curr_node = curr_node.next
        return curr_node
    
    def insert_node(self, new_node, after_node): # Time: O(1)
        after_node.next = new_node
        if after_node == self.tail:
            self.tail = new_node

    def delete_node(self, after_node): # Time: O(1)
        if after_node != self.tail:
            after_node.next = after_node.next.next
        else:
            after_node.next = None
            self.tail = after_node
    
    def push(self, new_node): # Time: O(1)
        self.tail.next = new_node
        self.tail = new_node

    def unshift(self, new_node): # Time: O(1)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self): # Time: O(n)
        curr_node = self.head
        prev_node = None
        while curr_node.next:
            prev_node = curr_node
            curr_node = curr_node.next
        if prev_node:
            prev_node.next = None
            self.tail = prev_node
        else:
            self.head, self.tail = None, None

    def shift(self): # Time: O(1)
        self.head = self.head.next

    def __find_tail(self): # Time: O(n)
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        return curr_node


class DoublyListNode:
    def __init__(self, data=0, next=None, previous=None):
        self.data = data
        self.next = next
        self.previous = previous

class DoublyLinkedList:
    def __init__(self, head=None):
        self.head = head
        self.tail = self.__find_tail()
    
    def search_list(self, key): # Time: O(n)
        curr_node = self.head
        while curr_node and curr_node.data != key:
            curr_node = curr_node.next
        return curr_node
    
    def insert_node(self, new_node, ref_node, direction="f"): # Time: O(1)
        if direction == "f":
            ref_node.next = new_node
            new_node.previous = ref_node
            if ref_node == self.tail:
                self.tail = new_node
        elif direction == "b":
            ref_node.previous = new_node
            new_node.next = ref_node
            if ref_node == self.head:
                self.head = new_node
    
    def delete_node(self, ref_node, direction="f"): # Time: O(1)
        if direction == "f":
            if ref_node != self.tail:
                ref_node.next, ref_node.next.next.previous = ref_node.next.next, ref_node
            else:
                ref_node.next = None
                self.tail = ref_node
        elif direction == "b":
            if ref_node != self.head:
                ref_node.previous, ref_node.previous.previous.next = ref_node.previous.previous, ref_node
            else:
                ref_node.previous = None
                self.head = ref_node
    
    def push(self, new_node): # Time: O(1)
        self.tail.next = new_node
        new_node.previous = self.tail
        self.tail = new_node

    def unshift(self, new_node):  # Time: O(1)
        self.head.previous = new_node
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):  # Time: O(1)
        if self.tail.previous:
            self.tail.previous.next, self.tail = None, self.tail.previous
        else:
            self.head, self.tail = None, None
    
    def shift(self):  # Time: O(1)
        if self.head.next:
            self.head.next.previous, self.head = None, self.head.next
        else:
            self.head, self.tail = None, None

    def __find_tail(self): # Time: O(n)
        curr_node = self.head
        while curr_node.next:
            curr_node = curr_node.next
        return curr_node


# Top Tips:
# -> Simple brute-force solution O(n) spaces can be reduced to O(1)
# -> cleanly coding rather than designing an algorithm will solve often
# -> Don't forget to update the next (and previous in doubly LL)
# -> LL algorithms often benefits for two iterators:
    # -> one ahead of another
    # -> one moving faster than another


# LL libraries:
# Own defined API should have the following minimum features:
    # -> returning head/tail
    # -> adding element at the head/tail
    # -> returning value stored at head/tail
    # -> deleting the head, tail or an arbitrary node

