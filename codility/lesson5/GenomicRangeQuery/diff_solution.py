# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(S, P, Q):
    # write your code in Python 3.6
    part_sum_s = [0, 0, 0, 0]
    counter = [[0, 0, 0, 0]]
    for s in S:
        if s == 'A':
            part_sum_s[0] += 1
            counter.append(part_sum_s[:])
        elif s == 'C':
            part_sum_s[1] += 1
            counter.append(part_sum_s[:])
        elif s == 'G':
            part_sum_s[2] += 1
            counter.append(part_sum_s[:])
        elif s == 'T':
            part_sum_s[3] += 1
            counter.append(part_sum_s[:])
    
    answer = []
    for p, q in zip(P, Q):
        arr = [b - a for a, b in zip(counter[p], counter[q+1])]
        for idx, num in enumerate(arr):
            if num:
                answer.append(idx+1)
                break
    
    return answer

print(solution('CAGCCTA', [2, 5, 0], [4, 5, 6]))