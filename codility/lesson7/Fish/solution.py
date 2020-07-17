# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, B):
    # write your code in Python 3.6
    N = len(A)
    stack = []
    for a, b in zip(A, B):
        if b == 0:
            while stack:
                if stack[-1] < a:
                    stack.pop()
                    N -= 1
                else:
                    N -= 1
                    break
                
        elif b == 1:
            stack.append(a)
    
    return N

print(solution([4, 3, 2, 1, 5], [0, 1, 0, 0, 0]))
# print(solution([4, 6, 1, 2, 5], [0, 1, 0, 0, 0]))
# print(solution([4, 3, 1, 2, 5, 7, 6], [0, 1, 0, 0, 0, 1, 0]))