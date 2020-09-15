from copy import deepcopy
def solution(tickets):
    n = len(tickets)
    def dfs(s, cnt):
        if cnt == n:
            return l
        for i in range(n):
            if visit[i]: continue
            if tickets[i][0] == s:
                visit[i] = 1
                l.append(tickets[i][1])
                r=dfs(tickets[i][1],cnt+1)
                print(r)
                l.pop()
                visit[i] = 0
        return r
    for i in range(n):
        visit = [0] * n
        l=['ICN']
        if tickets[i][0] == 'ICN':
            visit[i] = 1
            l.append(tickets[i][1])
            a = dfs(tickets[i][1], 1)
    return a


T = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
print(solution(T))