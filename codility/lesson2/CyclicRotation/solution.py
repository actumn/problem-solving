# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(A, K):
    # write your code in Python 3.6
    n = len(A)
    result = []
    for idx in range(-K, n-K):
        result.append(A[idx % n])
    return result

print(solution([1, 2, 3, 4], 4))
print(solution([3, 8, 9, 7, 6], 3))
print(solution([0, 0, 0], 1))
