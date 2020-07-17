# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(H):
    # write your code in Python 3.6
    N = len(H)
    
    stack = []
    answer = 0
    for num in H:
        while stack:
            if stack[-1] < num:
                answer += 1
                stack.append(num)
                break
            
            if stack[-1] == num:
                break
        
            if stack[-1] > num:
                stack.pop()
            
        if not stack:
            stack.append(num)
            answer += 1
            continue
        
    return answer
    
print(solution([8, 8, 5, 7, 9, 8, 7, 4, 8]))