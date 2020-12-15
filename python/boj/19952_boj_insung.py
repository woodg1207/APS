import sys; sys.stdin = open('s19952.txt', 'r')
from pprint import pprint

from collections import deque
tcs = int(input())
dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
for tc in range(tcs):
    H, W, O, F, Rs, Cs, Re, Ce = map(int, input().split())
    Rs, Cs, Re, Ce = Rs-1, Cs-1, Re-1, Ce-1
    arr = [[0]*W for _ in range(H)]
    visit = [[0]*W for _ in range(H)]
    visit[Rs][Cs] = 1
    for i in range(O):
        x, y, l = map(int, input().split())
        arr[x-1][y-1] = l
    q = deque()
    q.append((Rs, Cs, F))
    flag = 0
    while q:
        r, c, f = q.popleft()
        if r==Re and c==Ce:
            flag = 1
            break
        if not f:
            continue
        # visit[r][c] = 1
        for i in range(4):
            nr, nc = r+dr[i], c+dc[i]
            if 0<=nr<H and 0<=nc<W:
                if visit[nr][nc]: continue
                if f<arr[nr][nc]-arr[r][c]: continue
                visit[nr][nc] = 1
                q.append((nr, nc, f-1))
    if flag:
        print('잘했어!!')
    else:
        print('인성 문제있어??')
# dfs로 하면 시간 초과.
# def dfs(r, c, f):
#     w = 0
#     # print(r, c, f)
#     if r==Re and c == Ce: return 1
#     if f<=0: return 0
#     for i in range(4):
#         nr, nc = r + dr[i], c + dc[i]
#         if 0<=nr<H and 0<=nc<W:
#             if visit[nr][nc]: continue
#             if arr[r][c]<arr[nr][nc]: # jump
#                 if f < arr[nr][nc]-arr[r][c]: continue
#             visit[nr][nc] = 1
#             w+=dfs(nr, nc, f-1)
#             visit[nr][nc] = 0
#             if w: return w
#     return w
    # if dfs(Rs, Cs, F):
    #     print('잘했어!!')
    # else:
    #     print('인성 문제있어??')
