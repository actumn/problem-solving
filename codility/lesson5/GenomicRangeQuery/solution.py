# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    num_s = []
    answer = []
    for s in S:
        if s == 'A':
            num_s.append(1)
        elif s == 'C':
            num_s.append(2)
        elif s == 'G':
            num_s.append(3)
        elif s == 'T':
            num_s.append(4)
    
    for p, q in zip(P, Q):
        answer.append(min(num_s[p:q+1]))
    
    return answer