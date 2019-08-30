def permutations(master_list): # Time: O(n!) - n choices, then n-1 choices, ...
    if len(master_list) <= 1:
        return [master_list]

    el = master_list[0]
    rest = master_list[1:]
    perms_without = permutations(rest)

    perms_with = []
    for perm in perms_without:
        for i in range(len(perm)+1):
            perms_with.append(perm[:i] + [el] + perm[i:])
    
    return perms_with


print(permutations(["a", "b", "c"]))
