# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    set_A = set([i+1 for i in range(100000)])
    
    for num in A:
        set_A.discard(num)
        
    return next(iter(set_A))
