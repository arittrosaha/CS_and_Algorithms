# Divide-and-conquer is not synonymous with recursion. 

# Divide-and-conquer - smaller independent same type problem
# Recursion - more general
    # may be a single subproblem - binary search
    # non-independent subproblem - dynamic programming
    # not the same type as the original - regular expression matching

# Iterative divide-and-conquer over recursion can reduce space complexity and improve runtime

# Euclidean Algorithm for finding the greatest common divisor (GCD)
# Proof ref -> https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm

def gcd_recur(x, y): # Time: O(log(max(x, y))) ; Space: O(h), h is the depth of the call stacks
    if y == 0:
        return x
    else:
        return gcd_recur(y, x % y)

def gcd_iter(x, y): # Time: O(log(max(x, y))) ; Space: O(1)
    while y > 0:
        prev_y = y
        y = x % y
        x = prev_y
    return x

# print(gcd_recur(156, 36))
# print(gcd_iter(36, 156))
# print(gcd_iter(156, 36))

