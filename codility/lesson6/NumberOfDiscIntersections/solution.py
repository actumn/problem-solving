# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")
import bisect

def solution(A):
    # write your code in Python 3.6
    N = len(A)
    starts, ends = [], []
    for idx, num in enumerate(A):
        starts.append(idx - num)
        ends.append(idx + num)
    
    starts.sort()
    ends.sort()
    
    answer = 0
    for i, end in enumerate(ends):
        num = bisect.bisect(starts, end)
        answer += num - 1 - i
        if answer > 10000000:
            return -1
    
    return answer


print(solution([1, 5, 2, 1, 4, 0]))

