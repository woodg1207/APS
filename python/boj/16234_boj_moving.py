import sys; sys.stdin=open('s16234.txt', 'r')
from pprint import pprint

import sys
sys.setrecursionlimit(100000)
N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
c = 0
def dfs(r, c):
    visit[r][c] = True
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<N and 0<=nc<N:
            if visit[nr][nc]:continue
            if L<=abs(arr[r][c]-arr[nr][nc])<=R:
                union.append([nr, nc])
                dfs(nr, nc)
while 1:
    visit = [[False]*N for _ in range(N)]
    unions = []
    union = []
    for i in range(N):
        for j in range(N):
            if visit[i][j]: continue
            dfs(i, j)
            if len(union):
                union.append([i, j])
                unions.append(union)
            union = []
    if unions:
        c += 1
        for union in unions:
            value = 0

            for j in union:
                value+=arr[j[0]][j[1]]
            for j in union:
                arr[j[0]][j[1]] = value//len(union)
    else:
        print(c)
        break