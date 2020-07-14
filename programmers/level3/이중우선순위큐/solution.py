import heapq

def solution(operations):
    h = []
    maxh = []
    lastop = ''
    for op in operations:
        lastop = op
        if op[0] == 'I':
            heapq.heappush(h, int(op[2:]))
        elif op == 'D 1':
            if h:
                h.pop(h.index(max(h)))
        elif op == 'D -1':
            if h:
                heapq.heappop(h)
            
    if not h:
        return [0, 0]
    return [max(h), min(h)]

print(solution(["I 16", "I -5643", "D -1", "D 1", "D 1", "I 123", "D -1"]))
print(solution(["I -45", "I 653", "D 1", "I -642", "I 45", "I 97", "D 1", "D -1", "I 333"]))