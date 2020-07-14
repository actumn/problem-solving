import math

def solution(progresses, speeds):
    days = [math.ceil((100 - progress) / speed) for progress, speed in zip(progresses, speeds)]

    max_value = 0
    count = 0
    n = len(days)
    answer = []
    for idx in range(n):
        if days[idx] > max_value:
            answer.append(count)
            max_value = days[idx]
            count = 1
        else:
            count += 1
    answer.append(count)
        
    return answer[1:]

print(solution([93, 30, 55], [1, 30, 5]))