# Implement an ISBN cache

# Background:
# -> The International Standard Book Numberv(ISBN) is a unique commercial book identifier. 
# -> It is a string of length 10. 
# -> The first 9 characters are digits; the last character is a check character. 
# -> The check character is the sum of the first 9 digits, mod 11, with 10 represented by 'X'.
# -> Modern ISBNs use 13 digits, and the check digit is taken mod 10; this problem is concerned with 10-digit ISBNs.

# Prompt:
# -> Create a LRU cache for looking up prices of books identified by ISBN
# -> If an ISBN is already present, insert should not change the price, but it should update that entry to be the most recently used entry
# -> Lookup should also update that entry to be the most recently used entry.

import collections

class LRUcache:
    def __init__(self, capacity):
        self._isbn_price_table = collections.OrderedDict()
        self._capacity = capacity
    
    def lookup(self, isbn):
        if isbn not in self._isbn_price_table:
            return -1
        # the item is popped from is original location, then gets added at the end. 
        # basically right hand side is most recently used item
        price = self._isbn_price_table.pop(isbn)
        self._isbn_price_table[isbn] = price
        return price
    
    def insert(self, isbn, price):
        if isbn in self._isbn_price_table:
            price = self._isbn_price_table.pop(isbn)
        elif len(self._isbn_price_table) == self._capacity:
            self._isbn_price_table.popitem(last = false)

        self._isbn_price_table[isbn] = price

    def erase(self, isbn):
        # the second argument of pop basically acts as the default value if the key is not found
        return self._isbn_price_table.pop(isbn, None) is not None 