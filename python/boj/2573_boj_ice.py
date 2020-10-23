import sys; sys.stdin = open('s2573.txt','r')

import sys; sys.setrecursionlimit(10**9)

from collections import deque
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
Y = 0
flag = 0
memo = []
dr = (1, 0, -1, 0)
dc = (0, 1, 0, -1)

def dfs(r, c):
    visit[r][c] = True
    water = 0
    for i in range(4):
        nr, nc = r + dr[i], c + dc[i]
        if 0<=nr<N and 0<=nc<M:
            if visit[nr][nc]: continue
            if arr[nr][nc]:
                dfs(nr, nc)
            else:
                water += 1
    memo.append((r, c, water))

while 1:
    visit = [[False] * M for _ in range(N)]
    cnt_dfs = 0
    for i in range(N):
        for j in range(M):
            if visit[i][j]: continue
            if arr[i][j]:
                cnt_dfs += 1
                if cnt_dfs>1:
                    flag = 1
                    break
                # dfs(i, j)
                q = deque()
                q.append((i, j))
                visit[i][j] = True
                while q:
                    r, c = q.popleft()
                    # visit[r][c] = True
                    water = 0
                    for d in range(4):
                        nr, nc = r + dr[d], c + dc[d]
                        if 0<=nr<N and 0<=nc<M:
                            if visit[nr][nc]: continue
                            if arr[nr][nc]:
                                q.append((nr, nc))
                                visit[nr][nc] = True
                            else:
                                water += 1
                    memo.append((r, c, water))
        if flag:
            break
    else:
        if not cnt_dfs:
            flag = 2
    if not flag:
        for info in memo:
            arr[info[0]][info[1]] -= info[2]
            if arr[info[0]][info[1]] < 0:
                arr[info[0]][info[1]] = 0
    if flag:
        if flag == 2:
            print(0)
            break
        print(Y)
        break
    Y += 1
    memo.clear()