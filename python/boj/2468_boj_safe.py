import sys; sys.stdin = open('s2468.txt', 'r')
from pprint import pprint

import sys
sys.setrecursionlimit(10**6)
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

def dfs(r, c):
    visit[r][c] = True
    for d in range(4):
        nr, nc = r+dr[d], c+dc[d]
        if 0<=nr<N and 0<=nc<N:
            if visit[nr][nc]: continue
            if arr[nr][nc]>water:
                dfs(nr,nc)

m = 1
for water in range(1,101):
    visit=[[False]*N for _ in range(N)]
    cnt = 0
    for i in range(N):
        for j in range(N):
            if visit[i][j]:continue
            if arr[i][j] > water:
                cnt += 1
                dfs(i,j)
    if cnt == 0:
        break
    if m < cnt:
        m = cnt

print(m)