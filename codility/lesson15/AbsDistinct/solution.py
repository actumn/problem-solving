# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    a = set()
    for num in A:
        a.add(abs(num))
    return len(a)