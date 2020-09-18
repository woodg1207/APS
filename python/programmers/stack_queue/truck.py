from collections import deque
def solution(bridge_length, weight, truck_weights):
    bridge = deque()
    truck = deque()
    truck.extend(truck_weights)
    n = len(truck_weights)
    time_total = 0
    bridge.append([truck.popleft(), 1])
    while bridge:
        w = 0
        time_total += 1
        for i in range(len(bridge)):
            w += bridge[i][0]
        if len(truck)!=0:
            if w + truck[0] <= weight:
                bridge.append([truck.popleft(), 1])
        for i in range(len(bridge)):
            bridge[i][1] += 1
        if bridge[0][1]>bridge_length:
            bridge.popleft()
        if len(truck)!=0:
            if not bridge:
                bridge.append([truck.popleft(),1])
    return time_total+1

B, W = 100, 100
T = [10,10,10,10,10,10,10,10,10,10]
print(solution(B, W, T))