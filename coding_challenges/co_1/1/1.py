import heapq

def common_minimum(A, B):
    heapq.heapify(A)
    heapq.heapify(B)

    for _ in range(min(len(A), len(B))):
        min_A = A[0]
        min_B = B[0]

        if min_A == min_B:
            return min_A
        elif min_A < min_B:
            heapq.heappop(A)
        elif min_B < min_A:
            heapq.heappop(B)

    return -1

arr_A_1 = [1,3,2,1]
arr_B_1 = [4,2,5,3,2]

print(common_minimum(arr_A_1, arr_B_1))

arr_A_2 = [2,1]
arr_B_2 = [3,3]

print(common_minimum(arr_A_2, arr_B_2))