# Array - contiguous block of memory to usually represent sequences

# Time complexity:
# -> Indexing : O(1)
# -> Reassignment : O(1)
# -> Insertion at the end : Amortized O(1)
# -> Deletion at any index : O(n-i), n is array's length and i is the index getting deleted
# -> Insertion at any index : O(n-i), n is array's length and i is the insertion index 

# Array boot camp
# Promt: Input is an array of integers, and they have to reordered so that even
# entries comes first followed by unclassified and odd, respectively. Solve in
# space complexity of O(1)

def even_odd(arr):
    even_idx, odd_idx = 0, len(arr) - 1

    while (even_idx < odd_idx):
        integer = arr[even_idx]
        if integer % 2 == 0:
            even_idx += 1
        else:
            arr[even_idx], arr[odd_idx] = arr[odd_idx], arr[even_idx]
            odd_idx -= 1
    
    return arr
    
print(even_odd([0,1,2,3,4,5,6,7,8,9])) # => [0, 8, 2, 6, 4, 5, 7, 3, 9, 1]

# -> when a even number is found, even_idx is incremented to see if the next integer
# is even or odd

# -> when an odd number is found, it is exchanged with the current odd_idx value. Since
# it is safe to say that the new odd_idx integer will be an odd number after the
# exchange, the odd_idx is decremented by 1

# -> But it is not always certain that after the exchange the new value at even_idx
# will be an even value. This is why the even_idx is not incremented after the
# exchange. 
    # -> However, if the new number is an even number, then line 20 will pass in the
    # following iteration and even_idx will be incremented
    # -> If the new number is still an odd number, line 22 will pass to make another
    # exchange to transfer the odd back of the array while also lowering the
    # odd_idx because for sure that index now have an odd number


# Top Tips for Arrays
# -> Use the array itself to reduce space to O(1)

# -> Right array insertion is better:
#    Left array insertion is slower than right array insertion

# -> Overwriting is better than deletion:
#    Deleting is slower because it requires moving all entries to the left 

# Python Array Libraries:

# -> Two types of python arrays:
    # 1) list - dynamic array
    # 2) tuple - list but immutable
 
# -> Instanting list:
    # [3, 5, 7, 11] => [3, 5, 7, 11]
    # [1] + [0] * 10 => [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    # List comprehension : list(range(9)) => [0, 1, 2, 3, 4, 5, 6, 7, 8]

# -> Checking if a value is present:
    # A = [3, 5, 7, 11]
    # -> 5 in A => True
    # -> 4 in A => False

# -> Shallow vs. deep copy:
    # A = [3, 5, 7, 11]
    # -> B = A ; shallow copy
    # -> B = A[:] ; shallow copy
    # -> B = list(A) ; deep copy

# -> Key Methods:
    # ref -> https://docs.python.org/3/tutorial/datastructures.html

    # A = [3, 5, 7, 11]
    # -> LENGTH: len(A) => 4
    
    # ADDING:
    # -> PUSHING an item: A.append(42) => [3, 5, 7, 11, 42]
    # -> PUSHING multiple items : A.extend([12, 3]) => [3, 5, 7, 11, 42, 12, 3]
    # -> INSERT:  A.insert(2, 1) => [3, 2, 7, 5, 11, 42, 12, 3]

    # REMOVING:
    # A = [3, 2, 7, 5, 11, 42]
    # -> POPING: 
        # A.pop() => [3, 2, 5, 7, 11]
        # A.pop(1) => [3, 5, 7, 11]
        # A.popleft() => [5, 7, 11]
    # -> DELETING:
        # del A[i] : deletes the ith element
        # del A[i:j] : deletes the slice
        # del A[:] : deletes all items
        # A.clear() : deletes all items
    
    # Item characteristics:
    # -> INDEX : A.index(x[, start[, end]]) => returns x's index if it exits or raises a ValueError if not found.
    # -> COUNT : A.count(x) => returns the number of times x appears in the list.

    # MIN AND MAX:
    # A = [3, 5, 7, 11, 42]
    # -> min(A) => 3
    # -> max(A) => 42

    # REVERSING:
    # A.reverse() : in place reserve or mutates the original array
    # reversed(A) : returns an iterator or a new array
    # A[::-1] => [7, 2, 5, 4, 3, 6, 1]

    # SORTING:
    # A.sort() : in place
    # sorted(A) : returns a copy

    # SLICE:
    # A = [1, 6, 3, 4, 5, 2, 7]
    # General syntax: A[i: j: k], i, j and k are optional
    #
    # -> A[2:4] => [3, 4]
    # -> A[2:] => [3, 4, 5, 2, 7]
    # -> A[:4] => [1, 6, 3, 4]
    # -> A[:-1] => [1, 6, 3, 4, 5, 2]
    # -> A[-3:] => [5, 2, 7]
    # -> A[-3:-1] => [5, 2]
    # -> A[1:5:2] => [6, 4]
    # -> A[5:1:-2] => [2, 4]
    
    # ROTATE: A[k:] + A[:k], rotates A by k to the left
    # -> A[2:] + A[:2] => [3, 4, 5, 2, 7] + [1, 6] => [3, 4, 5, 2, 7, 1, 6]

    # BISECT:
    # Background:
        # -> it is a module
        # -> it is intended to be used with sorted iterable or array
        # -> The purpose of Bisect algorithm is to find a position in list where an element needs to be inserted to keep
        #    the list sorted.
    # 
    # import bisect ; from bisect import bisect_left ; from bisect import bisect_right ; from bisect import bisect
    # bisect.bisect by default performs like bisect_right
    #
    # A = [3, 5, 7, 11, 42]
    #
    # -> last index:
        # bisect_left(a, 42)) # => 4
        # bisect_right(a, 42)) # => 5
    #
    # -> beyond last index:
        # bisect_left(a, 43)) # => 5
        # bisect_right(a, 43)) # => 5
    #   
    # -> before last index:
        # bisect_left(a, 11)) # => 3
        # bisect_right(a, 11)) # => 4
    #
    # binary search with bisect REF -> https://www.geeksforgeeks.org/binary-search-bisect-in-python/
    # insort REF -> https://www.geeksforgeeks.org/bisect-algorithm-functions-in-python/

# -> List comprehension:
    # ref -> https://python-3-patterns-idioms-test.readthedocs.io/en/latest/Comprehensions.html
    # it consists of the following parts:
        # 1) Output expression - an expression that yields the elements
        # 2) An input sequence and an iterator over it
        # 3) An optional logical condition over the iterator
    #
    # -> General Examples:
        # -> [x**2 for x in range(6)] => [0, 1, 4, 9, 16, 25]
        # -> [x**2 for x in range(6) if x % 2 == 0] => [0, 4, 16]
    #
    # -> Multiple levels of looping:
        # -> Creating product of sets:
            # A = [1, 3, 5] and B = ["a", "b"]
            # -> [(x, y) for x in A for y in B] => [(1, "a"), (1, "b"), (3, "a"), (3, "b"), (5, "a"), (5, "b")]
        #
        # -> Convert 2D list to 1D list:
            # M = [["a", "b", "c"], ["d", "e", "f"]]
            # -> [x for row in M for x in row] => ["a", "b", "c", "d", "e", "f"]
        #
        # -> Iterating over each entry in a 2D list:
            # M = [[1, 2, 3], [4, 5, 6]]
            # -> [[x**2 for x in row] for row in M] => [[1, 4, 9], [16, 25, 36]]
    #
    # Notes: 
        # -> can be written using map(), filter(), and lambdas
        # -> avoid more than two nested comprehension
        # -> sets and dicts also support list comprehension




        









                                 
