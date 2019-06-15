# Binary Number Terminalogy
# ref - https://www.electronics-tutorials.ws/binary/bin_2.html

# Number of bits	    Common Name
#              1	    Bit
#              4	    Nibble
#              8	    Byte
#             16	    Word
#             32	    Double Word
#             64	    Quad Word


# Number base conversion:
# ref -> https://www.electronics-tutorials.ws/binary/bin_2.html

# Base 2 -> Base 10:
# 10000000101
# == (1 * 2**10) + (0 * 2**9) + (0 * 2**8) + (0 * 2**7) + (0 * 2**6) + (0 * 2**5) + (0 * 2**4) + (0 * 2**3) + (1 * 2**2) + (0 * 2**1) + (1 * 2**0)
# == (1 * 2**10) + (1 * 2**2) + (1 * 2**0)
# == (2**10) + (2**2) + (2**0)
# == 1024 + 4 + 1
# == 1029

# Base 10 -> Base 2:
# 1029
# 1029 / 2 = 514 ; 1 (LSB - Least Significant Bit)
#  514 / 2 = 257 ; 0
#  257 / 2 = 128 ; 1
#  128 / 2 =  64 ; 0
#   64 / 2 =  32 ; 0
#   32 / 2 =  16 ; 0
#   16 / 2 =   8 ; 0
#    8 / 2 =   4 ; 0
#    4 / 2 =   2 ; 0
#    2 / 2 =   1 ; 0
#    1 / 2 =   0 ; 1 (MSB - Most Significant Bit)
# 10000000101
# ^         ^
# MSB     LSB


# Two's complement -> one's-complement of (x-1)
# 1) Negative numbers are written with a leading 1 instead of a leading 0.
#   -> So if you are using only 8 bits for your two's-complement numbers, then you treat patterns from 
#      "00000000" to "01111111" as the whole numbers from 0 to 127, and reserve "1xxxxxxx" for writing 
#      negative numbers. This means that negative numbers go all the way down to - 128 ("10000000").
# 2) A negative number, -x, is written using the bit pattern for (x-1) with all of the bits 
#    complemented(switched from 1 to 0 or 0 to 1).
#    -> - 1 is one's-complement(1 - 1) = one's-complement(0) = one's-complement("00000000") == "11111111"
#    -> -10 is one's-complement(10 - 1) = one's-complement(9) = one's-complement("00001001") = "11110110"

# PY note: Python doesn't use 8-bit numbers. It USED to use however many bits were native to your machine, 
# but since that was non-portable, it has recently switched to using an INFINITE number of bits. Thus the 
# number - 5 is treated by bitwise operators as if it were written "...1111111111111111111011". Therefore, 
# infinite series of 1 bits in a negative number.

# ref -> https://wiki.python.org/moin/BitwiseOperators
#     -> https://www.youtube.com/watch?v=4qH4unVtJkE&t


# Complements in general
# ref -> https://www.youtube.com/watch?v=mzGYu5qBFSE

# 9's complements substraction
# ref -> https://en.wikipedia.org/wiki/Method_of_complements
#     -> https://www.youtube.com/watch?v=ejUTuskVUX4

# Bit Operators:
# ref -> https://wiki.python.org/moin/BitwiseOperators

# x << y
# Returns x with the bits shifted to the left by y places(and new bits on the right-hand-side are zeros). 
# This is the same as multiplying x by 2**y.

# x >> y
# Returns x with the bits shifted to the right by y places. This is the same as //'ing x by 2**y.
# It does not left-side with zeros.

# x & y
# Does a "bitwise and". Each bit of the output is 1 if the corresponding bit of x AND of y is 1, otherwise 
# it's 0.

# x | y
# Does a "bitwise or". Each bit of the output is 0 if the corresponding bit of x AND of y is 0, otherwise 
# it's 1.

# ~ x
# Python1 - Returns the complement of x (just one's complement). The number you get by switching each 1 for a 0 and 
# each 0 for a 1. This is the same as -x - 1.
# Python3 - Returns two's complement


# x ^ y
# Does a "bitwise exclusive or". Each bit of the output is the same as the corresponding bit in x if that 
# bit in y is 0, and it's the complement of the bit in x if that bit in y is 1.



# Bitwise operation example:
# ref = https://www.tutorialspoint.com/python/bitwise_operators_example.htm

# a = 60            # 60 = 0011 1100
# b = 13            # 13 = 0000 1101
# c = 0

# c = a & b        # 12 = 0000 1100
# print "Line 1 - Value of c is ", c

# c = a | b        # 61 = 0011 1101
# print "Line 2 - Value of c is ", c

# c = a ^ b        # 49 = 0011 0001
# print "Line 3 - Value of c is ", c

# c = ~a           # -61 = 1100 0011
# print "Line 4 - Value of c is ", c

# c = a << 2       # 240 = 1111 0000
# print "Line 5 - Value of c is ", c

# c = a >> 2       # 15 = 0000 1111
# print "Line 6 - Value of c is ", c



# Masking
# ref = https://en.wikipedia.org/wiki/Mask_(computing)
# ref = https://wiki.python.org/moin/BitManipulation
# ref = https://stackoverflow.com/questions/31575691/what-is-a-bitmask-and-a-mask

# Testing/Quering a bit
# -> Turning off all the other bits using the bitwise AND
# -> The value is compared with 1
# -> If it is equal to 0, then the bit was off, but if the value is any other value, then the bit was on

#      10011101   10010101
# AND  00001000   00001000
#   =  00001000   00000000

def testBit(int_type, offset):
    mask = 1 << offset
    return(int_type & mask)


# Setting a subset of bits
# -> Y OR 1 = 1 and Y OR 0 = Y
# -> to make sure a bit is on, OR can be used with a 1
# -> To leave a bit unchanged, OR is used with a 0

#      10010101   10100101
#  OR  11110000   11110000
#   =  11110101   11110101

def setBit(int_type, offset):
    mask = 1 << offset
    return(int_type | mask)


# Extracting a subsets of bits
# -> Y AND 0 = 0 and Y AND 1 = Y
# -> The extracting subsets need to be ANDed with 1 to leave them as they were originally
# -> To leave the other bits turned off, they can be ANDed with 0

#      10010101   10100101
# AND  00001111   00001111
#   =  00000101   00000101


# Clearing bit
# -> create the opposite mask with ~
# -> when the opposite mask is ANDed will all return 0

#      10010101   10100101
# AND  01101010   01011010
#   =  00000000   00000000

# Clearing a bit
def clearBit(int_type, offset):
    mask = ~(1 << offset)
    return(int_type & mask)


# Toggling bit
# -> the opposite of what it currently is
# -> XOR returns 1 if and only if an odd number of bits are 1
# -> 1 XOR 1 = 0 and 0 XOR 1 = 1

#      10011101   10010101
# XOR  00001111   11111111
#   =  10010010   01101010

# Toggling a bit
def toggleBit(int_type, offset):
    mask = 1 << offset
    return(int_type ^ mask)


# Substracting in Bits
# ref -> https://www.youtube.com/watch?v=S9LJknZTyos

# Base 10 to Base 2
# print(bin(11)) # => 0b1011

# Base 2 to Base 10
# print(int("1011", 2)) # => 11

# Weird stuff of bin and int in Python 3:
# ref -> https://python-forum.io/Thread-Find-the-complement-of-a-number
#     -> https://stackoverflow.com/questions/21871829/twos-complement-of-numbers-in-python
