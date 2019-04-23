# Parity of a word
# -> can be either 0 or 1
    # -> 1 : the word has odd number of 1s
    # -> 0 : the word has even number of 1s
# -> purposes : detect single bit errors in data storage and communication


def parity_v1(x): # brute force ; O(n), n is the word's size
    result = 0 
    while x:
        result ^= x & 1
        x >>= 1
    return result

# -> 1 flips result's previous result's value 
    # -> odd number of 1's makes the last result to be 1 (i.e. 0 => 1 -> 0 -> 1)
    # -> even number of 1's makes the last result to be 0 (i.e. 0 => 1 -> 0 -> 1 -> 0)
# -> 0 maintains previous result's value

# Example:
# x = 10011010 => parity will be 0 because even number of 1's

# Breakdown:
# result = 0

# result = result ^ (10011010 & 1) # 0 maintains previous result's value
# result = 0 ^ (10011010 & 1)
#        = 0 ^ 0
#        = 0
# x = 10011010 >> 1 = 1001101
# result = 0 ^ (1001101 & 1) # 1 flips result's value (0 to 1)
#        = 0 ^ 1
#        = 1
# x = 1001101 >> 1 = 100110  
# result = 1 ^ (100110 & 1) # 0 maintains previous result's value
#        = 1 ^ 0
#        = 1
# x = 100110 >> 1 = 10011  
# result = 1 ^ (10011 & 1) # 1 flips result's value (1 to 0)
#        = 1 ^ 1
#        = 0
# x = 10011 >> 1 = 1001
# result = 0 ^ (1001 & 1)  # 1 flips result's value (0 to 1)
#        = 0 ^ 1
#        = 1 
# x = 1001 >> 1 = 100
# result = 1 ^ (100 & 1)  # 0 maintains previous result's value
#        = 1 ^ 0
#        = 1
# x = 100 >> 1 = 10
# result = 1 ^ (10 & 1)  # 0 maintains previous result's value
#        = 1 ^ 0
#        = 1 
# x = 10 >> 1 = 1
# result = 1 ^ (1 & 1)  # 1 flips result's value (1 to 0)
#        = 1 ^ 1
#        = 0
# x = 1 >> 1 = 0



def parity_v2(x): # O(k); k is the number of bits set to 1
    result = 0
    while(x):
        result ^= 1 
        x &= x - 1
    return result

# -> x & (x - 1) equals x with its lowest set bit erased
# x                                 =   00101100
# x - 1                             = & 00101011
# x & (x - 1) = 00101100 & 00101011 =   00101000

# foot note : x & ~(x - 1) isolates the lowest bit that is 1 in x

# -> If there are even number of 1s, then an even number of iteration will take place until x becomes all 0s.
#    Then the result will get XORed an even number of times resulting it to be 0 at its last iteration.
# -> If there are odd number of 1s, then an odd number of iteration will take place until x becomes all 0s.
#    Then the result will get XORed an odd number of times resulting it to be 1 at its last iteration.


def parity_v3(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF 
    PRECOMPUTED_PARITY = "It should be a cache of all 16-bit words' parity but, for now, is a string to make the linter shut up"
    return (
        PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^
        PRECOMPUTED_PARITY[x >> (2 * MASK_SIZE) & BIT_MASK] ^
        PRECOMPUTED_PARITY[x >> MASK_SIZE & BIT_MASK] ^
        PRECOMPUTED_PARITY[x & BIT_MASK]
    )

# '0x' indicates its a hexadecimal. FFFF (Base 16) -> 1111111111111111 (Base 2) -> 65536 (Base 10)
# ref -> https://stackoverflow.com/questions/13137151/why-use-0xffff-over-65535

# GLOBAL_CONSTANT_NAME is the naming convention used in line 77, 78 and 79.
# ref -> https://stackoverflow.com/questions/159720/what-is-the-naming-convention-in-python-for-variable-and-function-names

# Point 1 -> Bit parity computation is associative - doesn't matter how its grouped
# Point 2 -> XOR is associative and comutative - doesn't matter how its grouped or ordered, respectively

# So to increase efficiency:
# 1) process multiple bits at a time
# 2) caching results in an array-based lookup table 
    # -> caching all 64-bit int will need 2^64 bits storage or 2 exabytes
    # -> caching all 16-bit int will need just 2^16 bits storage or 65536

# Example with 2-bit words:
# -> [0, 1, 1, 0] parity values for 00, 01, 10, 11 respectively 
    # -> 11 is the highest base 2 number with 2-bits storage
# -> 11001010 in 2-bit words 11, 00, 10, 10
# -> parity values based on lookup table is 0, 0, 1, 1 respectively
# -> final parity value is 0 because parity of 0, 0, 1, 1 as a group is 0
    # -> Because of Point 1 & 2

# -> to get first 2 bits out of 8, right shift by 6 : 11101010 >> 6 : 11101010 >> 2*3 : 00000011
# -> to get second 2 bits right shift by 4 : 11101010 >> 4 : 11101010 >> 2*2 : 00001110
# -> to hide the leading 11, mask by 1 with a mask size equal to subword's length : 
#    00001110 & 00000011 : 00000010

# Time Complexity: O(n/L)
# -> L be the width of the subwords
# -> n be the word's size
# -> so there will be n/L terms to look up from the cache with will O(1)


def parity_v4(x): # O(log n), n is the word size
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1

# print(parity_v4(11)) # 11 (base 10) -> 1011 (base 2) -> 1
# print(parity_v4(136)) # 136 (base 10) -> 10001000 (base 2) -> 0

# Big O can be even better by implementing parity_v3 table lookup after 16-bit

# -> Point 1: the parity of <b63,..., b0> == 
#             the parity of <b63,...,b32> ^ the parity of <b31,...,b0>
# -> Point 2: How to XOR the two 32-bits words together?
    # -> 1) right shift the original word 32 to get first 32-bits to be in place of 
    #    the last 32-bits positions .
    # -> 2) then XOR the shifted word with the original word because it has the 
    #    original b31 to b0 in their respective bit places.
# -> Point 3: leading bits are meaningless in this context, so the least
#             significant bit is a result and thus needs to be extracted.
    
# 1)         <b63,...,b0> >> 32 == <0(63th),...,0(32th), b63,...,b32>
# 2) XOR(^)                           <b63 ,..., b32,    b31,...,b0>
# 3)                               meaningless portion | meaningfull portion

# -> Point 4: The operation can be repeated from 32, 16, 8, 4, 2, 1-bit operands
#             to get the final result which is the least significant bit.

# Example: 8-bit word
# x = 11010111 (base 2)

# x = x ^ (x >> 4)
# x = 11010111 ^ (11010111 >> 4)
# x = 11010111 ^ 00001101         | 0111 ^ 1101
# x = 11011010                    | 1010

# x = 11011010 ^ (11011010 >> 2)
# x = 11011010 ^ 00110110         | 10 ^ 10
# x = 11101100                    | 00

# x = 11101100 ^ (11101100 >> 1)
# x = 11101100 ^ 01110110         | 0 ^ 0
# x = 10011010                    | 0

# x & 0x1 
# 10011010 & 00000001 
# 00000000

# 

# Time Complexity comparisons: 
# -> parity_v2 is very fast over parity_v1 when inputs have 1 sparsely
# -> parity_v2 is 20% faster over parity_v1 for random inputs
# -> parity_v3 is 4 times faster over parity_v2
# -> parity_v4 is 2 times faster over parity_v3



# Variants:
# 1) Right propagate the rightmost set bit in x     e.g. 80 (01010000) to 95 (01011111)
def right_propagate(x):
    lowest_set_bit = x & ~(x-1)
    subs_by_one = (x-1)
    return lowest_set_bit ^ subs_by_one

# print(right_propagate(80)) # => 95

# 1: first x needs to be substracted by 1 to get all the right most 0s to 1s
    # -> but that turns the lowest set bit to zero
# 2: so we need to toggle that bit back to 1
    # 2a : first exract the lowest set bit
    # 2b : then XOR the extraction with (x-1) to toggle the 0 back to 1

# 1:
# x                     = 01010000
# x-1                   = 01001111
# ~(x-1)                = 10110000

# 2a:
# x & ~(x-1):
# x                     :   01010000
# ~(x-1)                : & 10110000
#                       =   00010000

# 2b:
# (x & ~(x-1)) ^ (x-1):
# (x & ~(x-1))          :   00010000
# (x-1)                 : ^ 01001111
#                       =   01011111



# 2) Compute x mod a power of 2                     e.g. 13 for 77 mod 64
def mod_power_of_2(x, power_of_2):
    mod_mask = power_of_2 - 1
    return x & mod_mask

# print(mod_power_of_2(77, 64)) # => 13

# Background:
# if 12345 % 100, then extracting the last 2 digits will give us the remainder
# if 77 % 64 or 1001101 % 1000000, 
    # -> extracting the last 6 bits will give us the remainder because 64 is the
    #    7th binary place. 
    # -> In other words 64 (1000000) went into 77 (1001101) once and the remaining 
    #    more value 13 (001101) is the remainder which is the 6 least bits

# 1: 
# dynamic way to generate a mask based on what the power is or ith set bit is to 
# substract the power by 1 to fill the all right bits to 1s.
    # -> 64 (1000000) - 1 = 0111111

# 2:
# use the mask to extract the remaining more value or all the bits from i-1th bit
    # -> 1001101 & 0111111 = 0001101

# x = 77
# power_of_two = 64
# 77 % 64 or 1001101 % 1000000
# 1:
# mod_mask = 64 (1000000) - 1 = 0111111

# 2:
# x & mod_mask:
# x        :   1001101 (74)
# mod_mask : & 0111111 
#          =   0001101 (13)

# ref -> https://www.geeksforgeeks.org/compute-modulus-division-by-a-power-of-2-number/


# 3) Test if x is a power of 2                      e.g. true for x = 1,2,4,8,...
#                                                       false otherwise
def is_power_of_2(x):
    return ((x - 1) & x) == 0

# print(is_power_of_2(8)) # => True
# print(is_power_of_2(6)) # => False
# print(is_power_of_2(5)) # => False

# -> If x is a power of two, 
    # -> Its binary will have only one set bit
    # -> Therefore, toggling that one set bit to 0 would make the the whole number to zero
# -> If x is not a power of two,
    # -> Its binary will have more than one set bit
    # -> Therefore, will need more than one bit toggling to make the whole number zero

# Examples:

# x = 8; 2^3
# x             =  1000 (8)
# x - 1         =  0111 (7)
# (x - 1) & x   =  0000

# x = 6
# x             =  0110 (6)
# x - 1         =  0101 (5)
# (x - 1) & x   =  0100 (4)

# x = 5
# x             =  0101 (5)
# x - 1         =  0100 (4)
# (x - 1) & x   =  0100 (4)
