cache = {}
global_triangle = []
n = 0

def path(y, x):
    if y == n-1:
        return global_triangle[y][x]
    
    if (y,x) in cache:
        return cache[(y,x)]

    result = max(path(y+1, x), path(y+1, x+1)) + global_triangle[y][x]
    cache[(y,x)] = result
    return result

def solution(triangle):
    global n
    global global_triangle
    global_triangle = triangle
    n = len(triangle)
    
    return path(0, 0)

print(solution([[7], [3, 8], [8, 1, 0], [2, 7, 4, 4], [4, 5, 2, 6, 5]]))
