def custom_max(number):
    result = '0'
    idx = 0
    for i in range(len(number)):
        if number[i] > result:
            result = number[i]
            idx = i
    
    return result, idx

def solution(number, k):
    n = len(number)
    answer = []
    
    idx = 0
    for k_iterate in range(n-k):
        max_number, index = custom_max(number[idx:(k + k_iterate + 1)])
        idx = idx + index + 1
        answer.append(max_number)
        
        if idx == k + k_iterate + 1:
            break
    
    return ''.join(answer) + number[idx:]

print('solution', solution('1924', 2))
print('solution', solution('1231234', 2))
print('solution', solution('1231234', 3))
print('solution', solution('1231234', 6))
print('solution', solution('4177252841', 4))
