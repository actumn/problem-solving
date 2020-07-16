# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    result = [1 for _ in range(100001)]
    
    for num in A:
        if num < 1 or num > 100000: 
            continue
        
        result[num-1] = 0
    
    for idx, num in enumerate(result):
        if num:
            return idx + 1
    
    return 1
