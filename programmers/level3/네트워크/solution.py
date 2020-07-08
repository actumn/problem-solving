def solution(n, computers):
    trace = set()
    answer = 0
    
    for i in range(n):
        if i not in trace:
            answer += 1
            
            traverse(trace, computers, n, i)
            
    return answer

def traverse(trace, computers, n, i):
    trace.add(i)
    for idx in range(n):
        if idx not in trace and computers[i][idx] == 1:
            traverse(trace, computers, n, idx)
    
    return trace
    