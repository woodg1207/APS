import sys; sys.stdin=open('s16234.txt', 'r')

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]
c = 0
while(1):
    union = []
    visit = [[False]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(4):
                nr, nc = i + dr[k], j + dc[k]
                if 0<=nr<N and 0<=nc<N:
                    if visit[nr][nc]:
                        continue
                    if L<=arr[i][j]-arr[nr][nc]<=R:
                        visit[nr][nc]=True
                        union.append([nr, nc])
            print(visit, i, j)
            print(union)
    if len(union):
        s = 0
        for i, j in union:
            s += arr[i][j]
        result = s//len(union)
        print(s, result)
        for i, j in union:
            arr[i][j]=result
        print(arr)
        c += 1
    else:
        print(arr)
        print(c)
        break
    if c==4:
        break