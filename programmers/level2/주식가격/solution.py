def solution(prices):
    n = len(prices)
    answer = [i for i in reversed(range(n))]
    
    stack = []
    for idx, number in enumerate(prices):
        while stack:
            if stack[-1][1] > number:
                item = stack.pop()
                answer[item[0]] = idx - item[0]
            else:
                break
        
        stack.append((idx, number))
        
    return answer