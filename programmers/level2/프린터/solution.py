def solution(priorities, location):
    n = len(priorities)
    
    q = []
    current_idx = 0
    for priority in reversed(range(1, 10)):
        for idx in range(current_idx, current_idx+n):
            if priorities[idx % n] == priority:
                q.append(idx % n)
                current_idx = idx % n
            
    for order, idx in enumerate(q):
        if idx == location:
            return order + 1

    # not reach here
    return 0

print(solution([2, 1, 3, 2], 2))
print(solution([1, 1, 9, 1, 1, 1], 0))