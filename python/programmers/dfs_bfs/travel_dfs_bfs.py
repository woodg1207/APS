def convert(tickets, l):
    answer = []
    for i in l:
        result = []
        for idx in range(len(i)):
            if idx:
                result.append(tickets[i[idx]][1])
            else:
                result.extend(tickets[i[idx]])
        answer.append(result) 
    return answer
    
def solution(tickets):
    n = len(tickets)
    visit = [False for _ in range(n)]
    result = []
    def dfs(start, cnt):
        if n == cnt:
            result.append(l[:])
            return
        for i in range(n):
            if visit[i]: continue
            if tickets[i][0] ==start:
                visit[i] = True
                l.append(i)
                dfs(tickets[i][1], cnt+1)
                l.pop()
                visit[i] = False
    l = []
    for i in range(n):
        if tickets[i][0] == 'ICN':
            visit[i] = True
            l.append(i)
            dfs(tickets[i][1], 1)
            l.pop()
            visit[i] = False
    result = convert(tickets, result)
    return sorted(result)[0]



T = [['ICN' ,'B'], ['ICN', 'C'] ,['C', 'D'], ['D', 'ICN']]
T = [['ICN', 'A'], ['A', 'C'], ['A', 'D'], ['D', 'B'], ['B', 'A']]
T = [['ICN','A'],['ICN','A'],['A','ICN']]
T = [["ICN","BOO"], ["ICN", "COO"], [ "COO", "DOO" ], ["DOO", "COO"], [ "BOO", "DOO"] ,["DOO", "BOO"], ["BOO", "ICN" ], ["COO", "BOO"]]
T = [['ICN', 'JFK'], ['HND', 'IAD'], ['JFK', 'HND']]
T = [['ICN', 'SFO'], ['ICN', 'ATL'], ['SFO', 'ATL'], ['ATL', 'ICN'], ['ATL','SFO']]
print(solution(T))