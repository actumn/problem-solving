def solution(bridge_length, weight, truck_weights):
    q = [0] * bridge_length
    time = 0
    truck_sum = 0
    while q:
        time += 1
        truck_sum -= q.pop(0)
        if truck_weights:
            if truck_sum + truck_weights[0] <= weight:
                truck = truck_weights.pop(0)
                q.append(truck)
                truck_sum += truck
            else:
                q.append(0)
                
    return time

print(solution(2, 10, [7, 4, 5, 6]))
print(solution(100, 100, [10]))
