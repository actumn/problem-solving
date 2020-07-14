import heapq
from collections import deque

def solution(stock, dates, supplies, k):
    answer = 0
    h = []
    dates = deque(dates)
    supplies = deque(supplies)
    while stock < k:
        while dates and dates[0] <= stock:
            dates.popleft()
            heapq.heappush(h, -supplies.popleft())
        
        stock += -heapq.heappop(h)
        answer += 1
    return answer

print(solution(4, [4, 10, 15], [20, 5, 10], 30))
print(solution(4, [4, 10, 15, 30], [26, 5, 10, 10], 30))