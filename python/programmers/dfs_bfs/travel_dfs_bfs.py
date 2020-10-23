from copy import deepcopy
def solution(tickets):
    tickets = sorted(tickets, key=lambda t : t[1])
    n = len(tickets)
    x = []

    def dfs(d, cnt, l):
        if cnt == n:
            l.append(d)
            xx = deepcopy(l)
            x.append(xx)
            return
        
        for i in range(n):
            if visit[i]: continue
            if d == tickets[i][0]:
                visit[i] = True
                l.append(d)
                dfs(tickets[i][1], cnt + 1, l)
                l.pop()
                visit[i] = False

    for i in range(n):
        if tickets[i][0] == 'ICN':
            visit = [False] * n
            visit[i] = True
            dfs(tickets[i][-1], 1, ['ICN'])
    return x[0]


T = [['ICN' ,'B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']]
T = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
T = [['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]
T = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
T = [['ICN','A'],['ICN','A'],['A','ICN']]
T = [["ICN","BOO"], ["ICN", "COO"], [ "COO", "DOO" ], ["DOO", "COO"], [ "BOO", "DOO"] ,["DOO", "BOO"], ["BOO", "ICN" ], ["COO", "BOO"]]
print(solution(T))