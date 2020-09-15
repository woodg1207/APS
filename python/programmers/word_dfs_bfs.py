def solution(begin, target, words):
    n = len(begin)
    nw = len(words)
    combi = [[j for j in range(n) if i!=j] for i in range(n)]
    visit = [False]*nw
    l=[]
    def dfs(w, cnt):
        if w==target:
            l.append(cnt)
            return
        for i in range(nw):
            if visit[i]:continue
            for j in range(len(combi)):
                flag = 0
                for k in combi[j]:
                    if w[k]!=words[i][k]:
                        flag=1
                        break
                if flag: continue
                visit[i]=True
                dfs(words[i], cnt+1)
                visit[i]=False
        
    dfs(begin,0)
    if l: return min(l)
    return 0

B='hit'
T='cog'
W=['hot', 'dot', 'dog', 'lot', 'log', 'cog']	
print(solution(B,T,W))