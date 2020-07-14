def solution(m, n, puddles):
    global_map = []
    for _ in range(n+1):
        global_map.append([0] * (m+1))
    
    puddles = set([tuple(puddle) for puddle in puddles])
    
    global_map[1][1] = 1
    for x in range(1, m+1):
        for y in range(1, n+1):
            if x == 1 and y == 1:
                continue
            if (x, y) in puddles:
                continue
            
            global_map[y][x] = global_map[y-1][x] + global_map[y][x-1]

    return global_map[n][m] % 1000000007

print(solution(4, 3, [[2, 2]]))