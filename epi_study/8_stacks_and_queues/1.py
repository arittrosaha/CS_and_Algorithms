# Implement a stack with Max API

# Prompt 
# -> A stack that includes a max operation in addition to push and pop. 
# -> Max method should return the maximum value stored in the stack.


class Stack: # Space: O(1)
    def __init__(self, given_stack=[]):
        self.stack = given_stack
        if given_stack:
            self.global_max = max()
        else:
            self.global_max = None
    
    def push(self, passed_element): # Time: O(1)
        if passed_element > self.global_max:
            self.global_max = passed_element
        self.stack.append(passed_element)

    def max(self): # Time: O(n)
        curr_max = float("-inf")
        for element in self.stack:
            if element > curr_max:
                curr_max = element
        return curr_max
    
    def pop(self): # Time: O(n)
        if self.stack:
            popped_element = self.stack.pop()
            self.global_max = self.max()
            return popped_element
        else:
            return None



# For each entry in the stack, cache the maximum stored at or bellow that entry

import collections

class StackEPIv1: # Time: O(1); Space: O(n)
    # ref -> https://docs.python.org/3/library/collections.html#collections.namedtuple
    ElementWithCachedMax = collections.namedtuple("CacheElement", ("element", "max"))

    def __init__(self):
        # _ before properties are conventionally used to show internal properties 
        self._element_with_cached_max = []
    
    def empty(self):
        len(self._element_with_cached_max) == 0
    
    def max(self):
        if self.empty(): 
            raise IndexError("empty stack")
        return self._element_with_cached_max[-1].max
    
    def pop(self): # Time: O(1)
        if self.empty():
            raise IndexError("empty stack")
        return self._element_with_cached_max.pop().element
    
    def push(self, given_element): # Time: O(1)
        self._element_with_cached_max.append(
                given_element, 
                given_element if self.empty() else max(given_element, self.max())
            )



# If an element being pushed is smaller than the maximum element already in the stack, then e can never be the maximum 
# and thus no need to record it.

class StackEPIv2: # Time: O(1) ; Space: Worstcase O(n) to Bestcase O(1)
    class MaxWithCount:
        def __init__(self, max, count):
            self.max = max
            self.count = count
    
    def __init__(self):
        self._element = []
        self._cached_max_with_count = []
    
    def empty(self):
        return len(self._element) == 0

    def pop(self):
        if self.empty():
            raise IndexError("empty stack")
        popped_element = self._element.pop()
        if self._cached_max_with_count[-1].max == popped_element:
            self._cached_max_with_count[-1].count -= 1
            if self._cached_max_with_count[-1].count == 0:
                self._cached_max_with_count.pop()
        return popped_element

    def push(self, given_element):
        self._element.append(given_element)
        if len(self._cached_max_with_count) == 0:
            self._cached_max_with_count.append(self.MaxWithCount(given_element, 1))
        else:
            current_max = self._cached_max_with_count[-1].max
            if current_max == given_element:
                self._cached_max_with_count[-1].count += 1
            elif given_element > current_max:
                self._cached_max_with_count.append(self.MaxWithCount(given_element, 1))

