import sys; sys.stdin = open('s14502.txt', 'r')
from pprint import pprint

from collections import deque
from copy import deepcopy
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

visit = [[False]*M for _ in range(N)]
V = []
walls = []
max_v = 0
for i in range(N):
    for j in range(M):
        if arr[i][j]==2:
            V.append([i, j])
        elif arr[i][j] == 0:
            walls.append([i, j])
        else:
            visit[i][j] = True

for i in range(len(walls)):
    for j in range(i+1, len(walls)):
        for k in range(j+1, len(walls)):
            W = deepcopy(visit)
            for w in [i, j, k]:
                W[walls[w][0]][walls[w][1]] = True
            v = deque()
            v.extend(V)
            while v:
                r, c = v.popleft()
                W[r][c] = True
                for n in range(4):
                    nr, nc = r+dr[n], c+dc[n]
                    if 0<=nr<N and 0<=nc<M:
                        if W[nr][nc]: continue
                        W[nr][nc]=True
                        v.append([nr, nc])
            cnt = 0
            for idx in range(N):
                for jdx in range(M):
                    if not W[idx][jdx]:
                        cnt += 1
            if max_v<cnt:
                max_v = cnt
print(max_v)