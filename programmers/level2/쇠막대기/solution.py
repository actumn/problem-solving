
def solution(arrangement):
    x, count = 0, 0
    for idx in range(len(arrangement)):
        if arrangement[idx] == '(':
            x += 1
            count += 1
        elif arrangement[idx] == ')':
            if arrangement[idx-1] == '(':
                x -= 1
                count -= 1
                count += x
            else:
                x -= 1
        
    return count