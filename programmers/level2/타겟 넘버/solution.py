def solution(numbers, target):
    return solve(numbers, target, 0, 0)

def solve(numbers, target, index, num):
    if (index == len(numbers)):
        return 1 if target == num else 0
    
    return solve(numbers, target, index + 1, num + numbers[index]) + solve(numbers, target, index + 1, num - numbers[index])
    
print(solution([1, 1, 1, 1, 1], 3))