def make_2dvectors(n, airports, tickets):
    result = [[0 for _ in range(n)] for _ in range(n)]

    for ticket in tickets:
        here = ticket[0]
        there = ticket[1]
        result[airports.index(here)][airports.index(there)] += 1
    
    return result

def euler_circuit(n, paths, here, circuit):
    for there in range(n):
        while paths[here][there] > 0:
            paths[here][there] -= 1
            euler_circuit(n, paths, there, circuit)
    circuit.append(here)
    return circuit


def solution(tickets):
    airports = set()
    for ticket in tickets:
        airports.add(ticket[0])
        airports.add(ticket[1])

    n = len(airports)
    airports = list(airports)
    airports.sort()
    paths = make_2dvectors(n, airports, tickets)
    start = airports.index("ICN")

    circuit = euler_circuit(n, paths, start, [])

    answer = [airports[i] for i in reversed(circuit)]
    return answer

# print(make_2dvectors(3, ['SFO', 'ATL', 'ICN'], [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL", "SFO"]]))

print(solution([["ICN", "A"], ["A", "B"], ["B", "A"], ["A", "ICN"], ["ICN", "A"]]))
