# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    
    head_sum = [0] * N
    tail_sum = [0] * N
    max_sum = 0
    for idx in range(1, N-1):
        max_sum = max(0, max_sum + A[idx])
        head_sum[idx] = max_sum
    
    max_sum = 0
    for idx in reversed(list(range(1, N-1))):
        max_sum = max(0, max_sum + A[idx])
        tail_sum[idx] = max_sum
    
    print(head_sum)
    print(tail_sum)


print(solution([3, 2, 6, -1, 4, 5, -1, 2]))