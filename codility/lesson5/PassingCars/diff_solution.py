# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    ones = 0
    answer = 0
    for num in A:
        if num == 0:
            ones += 1
        else:
            answer += ones
    
    if answer > 1000000000:
        return -1

    return answer
