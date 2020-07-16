# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    n = len(A)
    arr = [1 for _ in range(n+1)]
    for num in A:
        arr[num-1] = 0
    
    for idx, num in enumerate(arr):
        if num:
            return idx + 1
    pass

print(solution([2, 3, 1, 5]))
