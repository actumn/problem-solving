# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S):
    # write your code in Python 3.6
    stack = []
    for s in S:
        if s == '(':
            stack.append(s)
            continue
        
        if s == ')' and stack and stack[-1] == '(':
            stack.pop()
            continue
        
        return 0
    
    if stack:
        return 0
        
    return 1