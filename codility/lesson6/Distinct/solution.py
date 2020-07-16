# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6]
    set_A = set()
    for a in A:
        set_A.add(a)
    
    return len(set_A)

print(solution([2, 1, 1, 2, 3, 1]))