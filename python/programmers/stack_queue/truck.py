from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    truck = deque()
    truck.extend(truck_weights)
    n = len(truck_weights)
    time_total = 0
    bridge.append([truck.popleft(), 1])
    while bridge:
        print(bridge, time_total)
        w = 0
        time_total += 1
        for i in range(len(bridge)):
            w += bridge[i][1]
        if len(truck)!=0 and w + truck[0] <= weight:
            bridge.append([truck.popleft(), 1])
        for i in range(len(bridge)):
            bridge[i][1] += 1
        if bridge[0][1]>=bridge_length:
            bridge.popleft()



    return time_total

B, W = 2, 10
T = [7, 4, 5, 6]
print(solution(B, W, T))