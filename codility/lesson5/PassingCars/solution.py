# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    zeros = []
    ones = []
    for idx, num in enumerate(A):
        if num == 0:
            zeros.append(idx)
        else:
            ones.append(idx)
            
    m, n = len(zeros), len(ones)
    
    curr_one_idx = 0
    answer = 0
    
    for zero_idx in zeros:
        while zero_idx > ones[curr_one_idx]:
            curr_one_idx += 1
        
        answer += n - curr_one_idx
        
        
    return answer

print(solution([0, 1, 0, 1, 1]))

print(solution([0, 0]))
