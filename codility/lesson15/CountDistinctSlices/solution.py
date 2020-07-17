# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(M, A):
    # write your code in Python 3.6
    record = [-1] * (M+1)
    
    N = len(A)
    result = 0
    count = 0
    front = 0
    for back, back_num in enumerate(A):
        while front < N and record[A[front]] == -1:
            record[A[front]] = front
            count += 1
            front += 1

        result += count
        count -= 1
        record[back_num] = -1
    
    
    return result
    
print(solution(6, [3, 4, 5, 5, 2]))
print(solution(6, [3, 4, 5, 4, 2]))
print(solution(6, [3]))
print(solution(0, [0]))
print(solution(0, [0, 0]))