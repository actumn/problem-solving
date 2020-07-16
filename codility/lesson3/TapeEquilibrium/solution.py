# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A):
    # write your code in Python 3.6
    part_sum = []
    n = len(A)
    sum_A = sum(A)
    culsum_A = 0
    for num in A:
        culsum_A += num
        part_sum.append(culsum_A)
    
    answer = 999999999999999
    for idx, num in enumerate(part_sum):
        if idx == n-1: break
        answer = min(answer, abs(sum_A - 2*num))
    
    return answer

print(solution([3, 1, 2, 4, 3]))