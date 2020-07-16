# you can write to stdout for debugging purposes, e.g.
# print("this is a debug message")

def solution(N):
    # write your code in Python 3.6
    chars = bin(N)[2:].strip('0').strip('1').split('1')
    return len(max(chars))

# print(solution(15))
print(solution(9))
print(solution(529))