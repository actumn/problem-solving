# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B, K):
    # write your code in Python 3.6
    b = B // K
    a = A // K
    if A % K == 0:
        return b - a + 1
    else:
        return b - a
