def num_of_actions(V):
    V = int(V, 2)
    count = 0
    while V:
        if V % 2 == 0:
            V /= 2
            count += 1
        else:
            V -= 1
            count += 1

    return count

print(num_of_actions("011100"))
