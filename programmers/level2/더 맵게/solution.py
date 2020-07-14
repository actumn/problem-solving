import heapq

def solution(scoville, K):
    h = []
    for item in scoville:
        heapq.heappush(h, item)
    
    cnt = 0
    while h[0] < K:
        if len(h) < 2: 
            return -1
        a = heapq.heappop(h)
        b = heapq.heappop(h)
        heapq.heappush(h, a + 2*b)
        cnt += 1

    return cnt
    
print(solution([1, 2, 3, 9, 10, 12], 7))
print(solution([1, 2, 9, 10, 12], 7))
print(solution([1, 2, 9, 10, 12], 10000))
