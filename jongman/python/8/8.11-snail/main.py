n, m = 0, 0
cache = {}

def climb2(days, climbed):
    if days == m:
        return 1 if climbed >= n else 0
    
    
    if (days, climbed) in cache:
        return cache[(days, climbed)]
    
    ret = 0.75 * climb2(days + 1, climbed + 1) + 0.25 * climb2(days + 1, climbed + 2)
    
    cache[(days, climbed)] = ret
    return ret