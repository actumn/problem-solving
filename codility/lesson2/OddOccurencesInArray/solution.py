# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
from collections import deque

def solution(A):
    # write your code in Python 3.6
    A = deque(A)
    x = set()
    for _ in range(len(A)):
        a = A.popleft()
        if a in x:
            x.remove(a)
        else:
            x.add(a)
    
    return next(iter(x))
