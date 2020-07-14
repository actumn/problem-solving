from collections import deque
import heapq
import math

def solution(jobs):
    jobs.sort(key=lambda x: x[0])
    if len(jobs) == 1:
        return jobs[0][1]

    jobs = deque(jobs)
    n = len(jobs)
    h = [(0, jobs.popleft())]
    time = h[0][1][0]
    answer = []
    while True:
        if not h and not jobs:
            break
        if not h:
            job = jobs.popleft()
            time = job[0]
            heapq.heappush(h, (job[1], job))
        item = heapq.heappop(h)
        while jobs and jobs[0][0] <= time + item[1][1]:
            job = jobs.popleft()
            heapq.heappush(h, (job[1], job))
        
        # print(item, time)
        answer.append(time + item[1][1] - item[1][0])
        time += item[1][1]

    # print(answer)
    return int(sum(answer) / n)

# print(solution([[0, 3], [1, 9], [2, 6]]))
# print(solution([[1, 3], [1, 9], [2, 6]]))
# print(solution([[0, 3], [4, 3], [10, 3]]))              # 3
# print(solution([[0, 10], [2, 3], [9, 3]]))              # 9
# print(solution([[1, 10], [3, 3], [10, 3]]))             # 9
# print(solution([[0, 10]]))                              # 10
# print(solution([[0, 10], [4, 10], [5, 11], [15, 2]]))   # 15
# print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 2], [15, 34], [35, 43], [26, 1]]))   # 74
print(solution([[24, 10], [18, 39], [34, 20], [37, 5], [47, 22], [20, 47], [15, 34], [15, 2], [35, 43], [26, 1]]))   # 74