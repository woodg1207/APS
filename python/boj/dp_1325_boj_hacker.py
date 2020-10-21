import sys; sys.stdin = open('s1325.txt', 'r')

import sys; sys.setrecursionlimit(1000000)
N, M = map(int, input().split())
info = [[0]] * (N + 1)
for i in range(M):
    a, b = map(int, input().split())
    if info[b][0] == 0:
        info[b] = [a]
    else:
        info[b].append(a)
memory = [[0]] * (N + 1)
hacking_max = 0

def dfs(com):
    visit[com] = 1
    if memory[com]!=[0]:
        return memory[com]
    c = [com]
    for i in info[com]:
        if i == 0: break
        if visit[i]: continue
        l = dfs(i)
        c.extend(l)
    memory[com] = c
    return c

result = []
for start in range(1, N + 1):
    visit = [0] * (N + 1)
    if memory[start]!=[0]:
        cnt = len(memory[start])
    else:
        cnt = len(dfs(start))
    if hacking_max<cnt:
        hacking_max = cnt
        result = [start]
    elif hacking_max==cnt:
        result.append(start)
print(*result)