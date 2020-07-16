# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    if N < 3:
        return 0
        
    A.sort()
    for i in range(2, N):
        if A[i-2] + A[i-1] > A[i]:
            return 1
    
    return 0
