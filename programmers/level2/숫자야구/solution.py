from itertools import permutations

pool = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
possible_numbers = list(map(''.join, permutations(pool, 3)))

def check_number(number, filter):
    strike = 0
    ball = 0
    for idx in range(3):
        if number[idx] == filter[idx]:
            strike += 1
        else:
            for idx2 in range(3):
                if idx == idx2:
                    continue
                if number[idx] == filter[idx2]:
                    ball += 1
    return strike, ball

def solution(baseball):
    answer = possible_numbers
    for filter in baseball:
        filtered = []
        filter_number = filter[0]
        strike = filter[1]
        ball = filter[2]
        for number in answer:
            if check_number(number, str(filter_number)) == (strike, ball):
                filtered.append(number)
        
        answer = filtered
            
    return len(answer)

print(solution(
  [[123, 1, 1], [356, 1, 0], [327, 2, 0], [489, 0, 1]]
))