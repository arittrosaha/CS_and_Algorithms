# The Towers of Hanoi problem

# Prompt: A program which prints a sequence of operations that transfers n rings from one peg to another.
    # There is a third initially empty peg.
    # Only a single ring from the top of one peg can be placed on the top of another peg
    # A larger ring must never be placed above a smaller ring

def compute_tower_hanoi(num_rings):
    NUM_PEGS = 3
    def compute_tower_hanoi_steps(num_rings_to_move, from_peg, to_peg, use_peg):
        if num_rings_to_move > 0:
            compute_tower_hanoi_steps(num_rings_to_move-1, from_peg, use_peg, to_peg)
            pegs[to_peg].append(pegs[from_peg].pop())
            result.append([from_peg, to_peg])
            compute_tower_hanoi_steps(num_rings_to_move-1, use_peg, to_peg, from_peg)
    
    result = []
    pegs = [list(reversed(range(1, num_rings + 1)))] + [[] for _ in range(1, NUM_PEGS)]
    compute_tower_hanoi_steps(num_rings, 0, 1, 2)
    return result

# print(compute_tower_hanoi(4))

# Time: O(2^n), for every call stack, we are making two more calls

# Logical understanding of the algorithm:

# ref -> https://en.wikipedia.org/wiki/Tower_of_Hanoi#Recursive_solution
# ref -> https://youtu.be/5_6nsViVM00?t=298

A = [3, 2, 1]
B = []
C = []

def move(n, source, auxiliary, target):
    if n > 0:
        # Step 1: move n - 1 disks from source to auxiliary, so they are out of the way
        move(n - 1, source, target, auxiliary)

        # Step 2: move the nth disk from source to target
        target.append(source.pop())

        # Display our progress
        print(A, B, C, '##############', sep='\n')

        # Step 3: move the n - 1 disks that we left on auxiliary onto target
        move(n - 1, auxiliary, source, target)


# initiate call from source A to target C with auxiliary B
move(3, A, B, C)
