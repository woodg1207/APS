import sys; sys.stdin = open('s2573.txt','r')

import sys; sys.setrecursionlimit(10**6)
from copy import deepcopy
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
Y = 0
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

def dfs(r, c):
    visit[r][c]=True
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<N and 0<=nc<M:
            if visit[nr][nc]: continue
            elif arr[nr][nc]<=0:
                dfs(nr,nc)
            elif arr[nr][nc]:
                visit[nr][nc]=True
                arr[nr][nc]-=1

def dfs2(r, c):
    visit1[r][c]=True
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<N and 0<=nc<M:
            if visit1[nr][nc]: continue
            elif arr[nr][nc]>0:
                dfs2(nr,nc)

while 1:
    Y+=1
    visit = [[False]*M for _ in range(N)]
    visit1 = deepcopy(visit)
    dfs(0,0)
    cnt = 0
    flag = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j]:
                if visit1[i][j]: continue
                dfs2(i,j)
                cnt += 1
            if cnt >1:
                flag = 1
                break
        if flag:
            break
    if flag:
        print(Y)
        break
    elif cnt == 0:
        print(0)
        break