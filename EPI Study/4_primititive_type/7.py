# Compute x^y
# prompt : Write a program that takes a double x and an integer y and returns x^y

# what is a double?
# -> generally, a double has 2 times the precision of float.
# ref -> https://stackoverflow.com/questions/2386772/what-is-the-difference-between-float-and-double

# -> in python, the built-in float type has double precision by default
# ref -> https://stackoverflow.com/questions/6663272/double-precision-floating-values-in-python

# x^(y0+y1) = x^y0 * x^y1

# x^10 = x^(5+5) = x^5             *   x^5 
#                = x^(4+1)         *   x^(4+1) 
#                = (x^4 * x)       +   (x^4 * x)
#                = (x^(2+2) * x)   +   (x^(2+2) * x)
#                = (x^2 * x^2 * x) +   (x^2 * x^2 * x)

# x^1010 = x^(101+101) = x^101             *   x^101
#                      = x^(100+1)         *   x^(100+1) 
#                      = (x^100 * x)       +   (x^100 * x)
#                      = (x^(10+10) * x)   +   (x^(10+10) * x)
#                      = (x^10 * x^10 * x) +   (x^10 * x^10 * x)

# So if y's (power) LSB is 0 (even) : (x^y/2)^2     = (x^y/2) + (x^y/2)
#                       is 1 (odd)  : x * (x^y/2)^2 = (x^y/2) + (x^y/2) * x

# If y is (-)ve replace : x with 1/x
#                       : y with -y

# Big(O) => O(n), n is the number of bits of y (power)

def power(x, y):
    result, power = 1, y
    if y < 0:
        x, power = 1.0/x, -power
    while power:
        if power & 1:
            result *= x
        x, power = x * x, power >> 1

    return result

# print(power(2, 10)) # => 1026
# x = 2, y = 10
# => x^y
# => 2^10 = (2^2)^(10/2)
# => 4^5  = 4^(4+1) = 4^4 * 4 = (4^2)^(4/2) * 4
# => 16^2 * 4 = 256 * 4 = 1026

# print(power(2, -2)) # => 0.25

def power_v2(x, y):
    if (y < 0):
        x, y = 1/x, -y

    if y == 2:
        return x * x
    elif y == 1:
        return x
    
    if y & 1:        
        return power_v2(x * x, y//2) * x
    else:
        return power_v2(x * x, y//2)

# print(power_v2(2, 10)) # => 1024
# print(power_v2(3, 3)) # => 27
# print(power_v2(2, -2)) # => 0.25