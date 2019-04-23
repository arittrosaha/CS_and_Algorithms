# counting the number of bits that are set to 1 in a nonnegative integer
def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits

# print(count_bits(5))

# x & 1 
# produces a value that is either 1 or 0, depending on the least significant bit of x: if the last bit is 1, 
# the result of x & 1 is 1 otherwise, it is 0. This is a bitwise AND operation.

# x >>= 1 
# means "set x to itself shifted by one bit to the right". The expression evaluates to the new value of x 
# after the shift.

# ref - https://stackoverflow.com/questions/38922606/what-is-x-1-and-x-1


# Know you primitive types

# 1) numerics -> integer
# 2) sequence -> list
# 3) mappings -> dict
# 4) classes
# 5) instances
# 6) exceptions

# all instances of these types are objects

import sys
# max bit size
    # PY 3 int are unbounded -> max int depends on available memory
    # sys.maxsize to find word-size which can used to find max value integer
        # 2**63 -1 on a 64 bit machine
        # print(sys.maxsize) # => 9223372036854775807
    # sys.float_info to find bounds on floats
        # print(sys.float_info)


# Signedness
# ref - https://www.computerhope.com/jargon/s/signedness.htm

# -> unsigned : an unsigned numeric value can represent a +(ve) or 0
    # -> an unsigned 8-bit numeric type can represent between 0 (00000000) to 255 (11111111)
# -> signed : a signed numeric value can represent +(ve), -(ve) and 0 
    # -> one of the bits of data is dedicated to represent "positive" or "negative"
    # -> a signed 8-bit number can represent -127 to 127. 
        # -> 7 of the bits are used for the binary representation of zero (0000000) through 127 (1111111)
        # -> 1 of the bits represents positivity or negativity
# -> signed can hold half as much as unsigned because it dedicates one bit for the number's sign. Thus the 
#    the highest possible number goes down by a factor of 2 for losing 1 bit.

# signed   8-bit :    0 (00000000) to 255 (11111111)
# unsigned 8-bit :    0 (0000000)  to 127 (1111111)  and 1 bit for the sign


# Commutative
# -> addition       : a + b = b + a 
# -> multiplication : ab = ba


# Associative
# -> addition       : a + (b + c) = (a + b) + c"
# -> multiplication : a(bc) = (ab)c


# Parrallel operation
    # -> Bit-level parallelism
        # -> Bit-level parallelism is a form of parallel computing based on increasing processor word size. 
        # -> Increasing the word size reduces the number of instructions the processor must execute in 
        #    order to perform an operation on variables whose sizes are greater than the length of the 
        #    word. 
        # -> For example, consider a case where an 8-bit processor must add two 16-bit integers. 
            # -> The processor must first add the 8 lower-order bits from each integer, then add the 8 
            #    higher-order bits, requiring two instructions to complete a single operation. 
            # -> A 16-bit processor would be able to complete the operation with single instruction.
        # -> ref - https://en.wikipedia.org/wiki/Bit-level_parallelism

    # -> Parallel algorithm
        # -> a parallel algorithm, as opposed to a traditional serial algorithm, is an algorithm which can 
        #    be executed a piece at a time on many different processing devices, and then combined together
        #    again at the end to get the correct result.
        # -> a parallel algorithm, as opposed to a traditional serial algorithm, is an algorithm which can
        #    be executed a piece at a time on many different processing devices, and then combined together 
        #    again at the end to get the correct result.
        # -> ref - https://en.wikipedia.org/wiki/Parallel_algorithm


# Integers have infinite precision
# Floats are not infinite precision

import math

# key methods for numeric types
print(abs(-34.5)) # => 43.5
print(math.ceil(2.17)) # => 3
print(math.floor(3.14)) # => 3
print(min(4, -4)) # => -4
print(max(3.14, 3)) # => 3.14
print(pow(2, 3)) # => 8
print(2**3) # => 8

# interconvert integers and strings
print(str(42) == "42") # => True
print(int("42") == 42) # => True

# interconvert floats and strings
print(str(3.14) == "3.14") # => True
print(float("3.14") == 3.14) # => True

# pseudo max-int and pseudo min-int
print(float("inf") > sys.maxsize) # => True
print(float("-inf") < -sys.maxsize) # => True

