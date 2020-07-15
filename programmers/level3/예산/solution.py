def solution(budgets, M):
    n = len(budgets)
    sum_budgets = sum(budgets)


    min_bound = 0
    max_bound = max(budgets)
    restrict = 0
    for _ in range(1000):
        sum_budgets = 0
        restrict = (min_bound + max_bound) // 2
        for budget in budgets:
            sum_budgets += min(restrict, budget)
        
        if sum_budgets < M:
            min_bound = restrict
        elif sum_budgets > M:
            max_bound = restrict
    
    return restrict

# print(solution([120, 110, 140, 150], 485))
print(solution([120, 110, 140, 150], 500))