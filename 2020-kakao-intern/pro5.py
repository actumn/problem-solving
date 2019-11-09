def solution(stones, k):
    answer = 0
    while True:
        for index in range(len(stones)):
            stones[index] = max(0, stones[index] - 1)
        
        answer += 1
            
        if calculate_max_zeroes(stones) >= k:
            break
            
            
    return answer

def calculate_max_zeroes(stones):
    result = 0
    count = 0 
    for index in range(len(stones)):
        if stones[index] == 0:
            count += 1
        
        if stones[index] != 0:
            result = max(result, count)
            count = 0
    
            
    return max(result, count)