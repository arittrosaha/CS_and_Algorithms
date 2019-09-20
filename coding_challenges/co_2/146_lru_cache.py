# ref -> https://leetcode.com/problems/lru-cache/


class DoublyLL:
    def __init__(self, value=None, prev=None, next=None):
        self.value = value
        self.prev = prev
        self.next = next

class LRUCache: # Time: O(1) ; Space: O(c)
    def __init__(self, capacity):
        self.cache = {}
        self.capacity = capacity
        self.head = DoublyLL()
        self.tail = DoublyLL()
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, element): # Time: O(1)
        if element in self.cache:
            self._move_to_head(self.cache[element])
            return self.cache[element].value
        else:
            return -1
    
    def _move_to_head(self, node): 
        curr_next = self.head.next
        
        if node.value in self.cache:
            node_prev = node.prev
            node_next = node.next
            node_prev.next = node_next
            node_next.prev = node_prev

        self.head.next = node
        node.prev = self.head
        node.next = curr_next
        curr_next.prev = node
        

    def put(self, element): # Time: O(1)
        if element not in self.cache:
            new_node = DoublyLL(element)
            if len(self.cache) >= self.capacity:
                curr_tail_prev = self.tail.prev
                curr_tail_prev.prev.next = self.tail
                self.tail.prev = curr_tail_prev.prev
                curr_tail_prev.next, curr_tail_prev.prev = None, None
                del self.cache[curr_tail_prev.value]
            self._move_to_head(new_node)
            self.cache[element] = new_node
    

# cache = LRUCache(2)
# cache.put(1)
# cache.put(2)
# print(cache.get(1)) # => 1
# cache.put(3) # evicts 2
# print(cache.get(2)) # => -1
# cache.put(4) # evicts 1
# print(cache.get(1)) # => -1
# print(cache.get(3)) # => 3
# print(cache.get(4)) # => 4


# For solution using python library, check the link bellow:
# ref -> https://leetcode.com/problems/lru-cache/solution/
    # ref -> https://docs.python.org/3/library/collections.html#collections.OrderedDict
