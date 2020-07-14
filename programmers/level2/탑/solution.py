def solution(heights):
    n = len(heights)
    answer = [0] * n
    for idx in reversed(range(n)):
        for idx2 in reversed(range(idx)):
            if heights[idx2] > heights[idx]:
                answer[idx] = idx2 + 1
                break
                
    return answer

print(solution([6, 9, 5, 7, 4]))
