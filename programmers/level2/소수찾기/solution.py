import math

numbers_len = 0
answer = set()

def is_prime(number):
    if number < 2:
        return False
    
    for num in range(2, int(math.sqrt(number)) + 1):
        if number % num == 0:
            print(number, num)
            return False
    
    return True
    

def permutation(numbers, taken, number):
    if len(number) == numbers_len:
        return
    
    for index in range(numbers_len):
        if taken[index] == 1:
            continue
        
        taken[index] = 1

        number = number + numbers[index]
        int_number = int(number)
        if is_prime(int_number):
            answer.add(int_number)
        
        permutation(numbers, taken, number)
        number = number[:-1]
        taken[index] = 0
    
    
    
def solution(numbers):
    global numbers_len
    numbers_len = len(numbers)
    taken = [0 for _ in range(numbers_len)]

    permutation(numbers, taken, "")
    
    return len(answer)