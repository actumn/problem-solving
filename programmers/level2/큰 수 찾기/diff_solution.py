def solution(number, k):
    if k == 0:
        return ''

    stack = [number[0]]

    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    
    if k != 0:
        stack = stack[:-k]

    return ''.join(stack)

print('solution', solution('1924', 2))
print('solution', solution('1231234', 2))
print('solution', solution('1231234', 3))
print('solution', solution('1231234', 6))
print('solution', solution('4177252841', 4))