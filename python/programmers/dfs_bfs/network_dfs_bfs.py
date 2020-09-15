def solution(n, computers):
    G = [[] for _ in range(n)]
    visit = [False]*n
    for i in range(n):
        for j in range(i+1, n):
            if computers[i][j]:
                G[i].append(j)
                G[j].append(i)
    cnt = 0
    def dfs(a):
        visit[a]=True
        for i in range(len(G[a])):
            if visit[G[a][i]]:continue
            dfs(G[a][i])

    for i in range(n):
        if visit[i]: continue
        dfs(i)
        cnt += 1
    return cnt

N=3
C = 	[[1, 1, 0], [1, 1, 0], [0, 0, 1]]
print(solution(N, C))