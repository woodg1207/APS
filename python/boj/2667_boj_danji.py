import sys; sys.stdin=open('s2667.txt','r')

from collections import deque
N = int(input())
arr = [list(map(int, input())) for _ in range(N)]
    
dr = [1,0,-1,0]
dc = [0,1,0,-1]

danji_list = []
for i in range(N):
    for j in range(N):
        if arr[i][j]:
            arr[i][j] = 0
            c = 1
            q = deque()
            q.append([i,j])
            while q:
                p = q.popleft()
                for d in range(4):
                    nr, nc = p[0]+dr[d], p[1]+dc[d]
                    if 0<=nr<N and 0<=nc<N:
                        if arr[nr][nc]:
                            q.append([nr,nc])
                            arr[nr][nc] = 0
                            c += 1
            danji_list.append(c)
print(len(danji_list))
for i in sorted(danji_list):
    print(i)