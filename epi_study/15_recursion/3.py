# Generate permutations

# Prompt:
# input - an array of distinct integers
# output - generates all permutations of that array
# constraints - no permutation of the array may appear more than once
#             - any ordering is acceptable

# Complexity:
    # Time - n x n!, each call is finished with n due to line 19 and there are n! calls
    # Space - n!, each call gets a new slice

def permutations(A):
    def perm_helper(remaining, n):
        if len(remaining) == 0:
            results.append(list(curr_perm))
            return 
        
        for i, num in enumerate(remaining):
            curr_perm[n] = num
            perm_helper(remaining[:i] + remaining[i+1:], n + 1)

    results, curr_perm = [], [None] * len(A)
    perm_helper(A, 0)
    return results

print(permutations([2,3,5,7]))


# Time: O(n!) ; Space: O(n!)
# PDF - 237

def permutations_epi(A):
    def directed_permutations(i):
        if i == len(A) - 1:
            result.append(A.copy())
            return
        for j in range(i, len(A)):
            A[i], A[j] = A[j], A[i] 
            directed_permutations(i+1)
            A[i], A[j] = A[j], A[i] 
    
    result = []
    directed_permutations(0)
    return result
