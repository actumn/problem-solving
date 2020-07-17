def solution(A):
    n = len(A)
    size = 0
    for num in A:
        if size == 0:
            size += 1
            value = num
            continue
        
        if value != num:
            size -= 1
        else:
            size += 1

    candidate = -1
    if size > 0:
        candidate = value
    
    count = 0
    idx = 0
    for k in range(n):
        if A[k] == candidate:
            count += 1
            idx = k
    if count > n // 2:
        return idx
    return -1

print(solution([3, 4, 3, 2, 3, -1, 3, 3]))