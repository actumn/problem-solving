
import sys
sys.setrecursionlimit(10**6)

g_left = []
g_right = []
cache = []

def find(l_idx, r_idx):
    if l_idx == len(g_left) - 1 and r_idx == len(g_right) - 1:
        if g_left[l_idx] > g_right[r_idx]:
            return g_right[r_idx]
        else:
            return 0
    elif l_idx == len(g_left) - 1:
        if g_left[l_idx] > g_right[r_idx]:
            result = g_right[r_idx] + find(l_idx, r_idx+1)
            return result
        else:
            return 0
    elif r_idx == len(g_right) - 1:
        if g_left[l_idx] > g_right[r_idx]:
            return g_right[r_idx]
        else:
            result = find(l_idx+1, r_idx)
            return result
        
    if cache[l_idx][r_idx] != -1:
        return cache[l_idx][r_idx]

    case1 = find(l_idx+1, r_idx)
    case2 = find(l_idx+1, r_idx+1)
    case3 = 0
    if g_left[l_idx] > g_right[r_idx]:
        case3 = g_right[r_idx] + find(l_idx, r_idx+1)
    
    result = max(case1, case2, case3)
    cache[l_idx][r_idx] = result
    return result

def solution(left, right):
    global g_left, g_right, cache
    g_left = left
    g_right = right
    cache = [[-1] * len(right) for _ in range(len(left))] 

    return find(0, 0)

print(solution([3, 2, 5, 1], [2, 4, 6]))