import sys; sys.stdin = open('s1325.txt', 'r')

from collections import deque
N, M = map(int, input().split())
info = [[0]] * (N+1)
for i in range(M):
    a, b = map(int, input().split())
    if info[b][0] == 0:
        info[b] = [a]
    else:
        info[b].append(a)
        
hacking_max = 0
result = []
for start in range(1, N+1):
    visit = [0] * (N+1)
    q = deque()
    q.append(start)
    while q:
        com = q.popleft()
        visit[com] = 1
        for i in info[com]:
            if i == 0: break
            if visit[i]: continue
            q.append(i)
            visit[i] = 1
    if sum(visit) > hacking_max:
        hacking_max = sum(visit)
        result = [start]
    elif sum(visit) == hacking_max and sum(visit):
        result.append(start)
print(*result)