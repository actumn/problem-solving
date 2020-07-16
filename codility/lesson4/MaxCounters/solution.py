# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N, A):
    # write your code in Python 3.6
    answer = [0] * N
    last_max = 0
    current_max = 0
    for num in A:
        if num == N+1:
            last_max = current_max
            continue
        answer[num-1] = max(last_max, answer[num-1])
        answer[num-1] += 1
        current_max = max(current_max, answer[num-1])
    
    for idx in range(N):
        answer[idx] = max(answer[idx], last_max)

    return answer

print(solution(5, [3, 4, 4, 6, 1, 4, 4]))
