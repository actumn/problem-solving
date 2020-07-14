def solution(N):
    case = [1, 1]
    for _ in range(N-1):
        case.append(case[-1] + case[-2])
    
    return (case[-1] + case[-2]) * 2