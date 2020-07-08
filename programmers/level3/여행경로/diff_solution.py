from collections import defaultdict
import copy

def dfs(start, table, arr, result, n_tickets): 
    #이동한 경로를 저장함 
    arr.append(start) 
    for i in range(len(table[start])): 
        #이미 방문했으면 건너뛴다
        if table[start][i] == True: 
            continue
        else :
            # 해당 경로에서 도착할 수 있는 다음 경로를 확인한다 
            next_des = table[start][i]
            # 다음 경로의 visited여부를 True로 반환한다.
            table[start][i] = True
            # 다음 경로에서 진행할 수 있는 여행경로를 탐색한다.
            temp = dfs(next_des, table, arr, result, n_tickets)
            # 주어진 항공권을 모두 사용해 경로를 만들 수 있는 경우
            if len(temp) == n_tickets + 1: 
                result.append(copy.deepcopy(temp))
            # 백트래킹 
            arr.pop() 
            table[start][i] = next_des
    # 해당 공항에서 더 이상 다음으로 진행할 수 없으면 저장한 경로를 반환
    return arr 

def solution(tickets): 
    #각 공항에서 다른 곳으로 이동할 수 있는 경우의 수 저장 
    table = defaultdict(list) 
    
    for value in tickets: 
        f, t = value[0], value[1] 
        table[f].append(t)
        
    # 방문할 수 있는 경로를 저장하는 배열 
    result = [] 
    dfs('ICN', table, [], result, len(tickets))
    # 알파벳 순서가 앞서는 경로 출력하기
    return sorted(result)[0]

print(solution([["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))
