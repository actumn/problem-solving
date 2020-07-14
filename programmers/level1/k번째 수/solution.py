def solution(array, commands):
    answer = []
    for command in commands:
        arr = array[command[0]-1:command[1]]
        arr.sort()
        k = command[2]
        answer.append(arr[k-1])
        
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))