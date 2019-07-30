# set
    # s.add(42)
    # s.remove(42)
    # s.discard(123)
    # x in s
    # s <= t -> is s a subset of t?
    # s - t -> elements in s that are not in t
# frozenset - immutable set
# dict
# collections.defaultdict
# collections.Counter - used of counting the number of occurrences of keys
    # c = collections.Counter(a=3, b=1)
    # d = collections.Counter(a=1, b=2)
    ## c + d -> {"a": 4, "b": 3}
    ## c - d -> {"a": 2} ; keeps only positive counts
    ## c & d -> {"a": 1, "b": 1} ; intersections
    ## c | d -> {"a": 3, "b": 2} ; union

# Default value:
    # dict -> accessing value associated with a non-existing key leads to a KeyError exception
    # collections.defaultdict -> returns the default value of the type that was specified
        # e.g. d = collections.defaultdict(list) ; d[k] is []

# Iterations:
    # items() -> iteration over key-value elements
    # values() -> iteration over values
    # keys() -> iterations over keys

# Mutables containers are not hashable - lookup will fail if the key is mutated because the modified object's hash will lead to a different slot

# Built-in hash() function simplifies when implementing hash function of a user-defined class, i.e. __hash__(self)

