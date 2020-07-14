def solution(N, number):
    cases = [0, {N}]
    
    for i in range(2, 9):
        case = {int(str(N) * i)}
        
        for idx in range(1, i // 2 + 1):
            for item1 in cases[idx]:
                for item2 in cases[i-idx]:
                    case.add(item1 + item2)
                    case.add(item1 - item2)
                    case.add(item2 - item1)
                    case.add(item1 * item2)
                    if item2 != 0:
                        case.add(item1 // item2)
                    if item1 != 0:
                        case.add(item2 // item1)
        
        if number in case:
            return i
        cases.append(case)
                
    return -1
# print(solution(5, 12))
print(solution(4, 17))