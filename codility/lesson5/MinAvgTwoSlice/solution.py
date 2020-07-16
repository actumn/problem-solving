# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    min_avg = (A[0] + A[1]) / 2
    min_idx = 0
    for i in range(2, len(A)):
        avg = (A[i-2] + A[i-1] + A[i]) / 3
        if min_avg > avg:
            min_avg = avg
            min_idx = i - 2
        
        avg = (A[i - 1] + A[i]) / 2
        if min_avg > avg:
            min_avg = avg
            min_idx = i-1
    
    return min_idx
