import sys; sys.stdin = open('s2636.txt','r')
import sys
sys.setrecursionlimit(10**6)

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]

hour = 0
memory = []

def dfs(r, c):
    visit[r][c] = True
    for i in range(4):
        nr, nc = r+dr[i], c+dc[i]
        if 0<=nr<N and 0<=nc<M:
            if visit[nr][nc]: continue
            elif arr[nr][nc] == 0:
                dfs(nr,nc)
            elif arr[nr][nc] == 1:
                visit[nr][nc] = True
                arr[nr][nc] = 0
                l.append([nr, nc])
                
while 1:
    hour += 1
    visit  = [[False]*M for _ in range(N)]
    l = []
    dfs(0,0)
    if not len(l):
        print(hour-1)
        print(memory.pop())
        break
    memory.append(len(l))

            