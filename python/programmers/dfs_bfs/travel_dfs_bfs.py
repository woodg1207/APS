from copy import deepcopy
def solution(tickets):
    n = len(tickets)
    xx = []
    def dfs(s, cnt, t):
        if cnt == n:
            xx.append(t)
            return t
        for i in range(n):
            if visit[i]: continue
            if tickets[i][0] == s:
                visit[i] = 1
                t.append(tickets[i][1])
                r=dfs(tickets[i][1],cnt+1, t)
                if r==0:
                    visit[i]=0
                    t.pop()
        try:
            return r
        except:
            return 0
    result = []
    for i in range(n):
        visit = [0] * n
        if tickets[i][0] == 'ICN':
            visit[i] = 1
            x=dfs(tickets[i][1], 1, ['ICN', tickets[i][1]])
            if x == 0: continue
            result.append(x)
    # print(result)
    print(xx)
    return sorted(result)[0]


T = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
T = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
T = [['ICN' ,'B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']]
T = [['ICN','A'],['ICN','A'],['A','ICN']]
T = [['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]
T = [["ICN","BOO"], ["ICN", "COO"], [ "COO", "DOO" ], ["DOO", "COO"], [ "BOO", "DOO"] ,["DOO", "BOO"], ["BOO", "ICN" ], ["COO", "BOO"]]
print(solution(T))