def solution(numbers):
    arr = list(map(str, numbers))   
    arr = sorted(arr, key=lambda x: x*4, reverse=True)
    return str(int(''.join(arr)))

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))