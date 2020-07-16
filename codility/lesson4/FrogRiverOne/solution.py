# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(X, A):
    # write your code in Python 3.6
    set_A = set()
    for idx, num in enumerate(A):
        set_A.add(num)
        if len(set_A) == X:
            return idx
    
    return -1

print(solution(5, [1, 3, 1, 4, 2, 3, 5, 4]))