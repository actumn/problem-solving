# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    arr = [1] * N
    for num in A:
        if num > N:
            continue
        arr[num-1] = 0
    
    for num in arr:
        if num:
            return 0
    return 1
