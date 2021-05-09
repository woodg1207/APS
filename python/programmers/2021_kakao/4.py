from collections import deque
def new_road(roads):
    temp = dict()
    for i in range(len(roads)):
        s, e, r =roads[i]
        try:
            if temp['{},{}'.format(s, e)]>r:
                temp['{},{}'.format(s, e)] = r
        except:
            temp['{},{}'.format(s, e)] = r
    result = []
    for k, v in temp.items():
        s, e = map(int, k.split(','))
        result.append([s,e,v])
    return result

def give_road(s, trap, roads):
    result = []
    if trap:
        for r in roads:
            if s == r[1]:
                result.append([r[1],r[0], r[2]])
            else:
                result.append(r)
        return result
    return roads

def solution(n, start, end, roads, traps):
    answer = 0
    roads = new_road(roads)
    l=[]
    loop=dict()
    def dfs(s, time, trap, road):
        road = give_road(s, trap, road)
        if s == end:
            l.append(time)
            return
        if l and time > min(l):
            return
        for r in road:
            if loop.get('{},{}'.format(r[0],r[1])) and loop['{},{}'.format(r[0],r[1])]>2:
                continue
            if r[0]==s:
                print(s, r, road, time, trap)
                if loop.get('{},{}'.format(r[0],r[1])):
                    loop['{},{}'.format(r[0],r[1])] += 1
                else:
                    loop['{},{}'.format(r[0],r[1])] = 1
                if r[1] in traps:
                    dfs(r[1], time+r[2], 1, road)
                else:
                    dfs(r[1], time+r[2], 0, road)
    dfs(start, 0, 0, roads)

    return min(l)
    

print(solution(3, 1, 3,	[[1, 2, 2], [3, 2, 3]], [2]))
print(solution(4, 1, 4,	[[1, 2, 1], [3, 2, 1], [2, 4, 1]],[2,3]))





    
    # q = deque()+r[2], 0))
    # q.append((start, 0, 0))
    # while q:
    #     s, time, tr = q.popleft()
    #     # print(s, time, tr )
    #     if s == end:
    #         l.append(time)
    #     if l:
    #         if min(l) < time:
    #             continue
    #     rs = give_road(s, tr, roads)
    #     # print(roads)
    #     for r in rs:
    #         if loop.get('{},{}'.format(r[0],r[1])) and loop['{},{}'.format(r[0],r[1])]>2:
    #             continue
    #         if r[0]==s:
    #             if loop.get('{},{}'.format(r[0],r[1])):
    #                 loop['{},{}'.format(r[0],r[1])] += 1
    #             else:
    #                 loop['{},{}'.format(r[0],r[1])] = 1
    #             if r[1] in traps:
    #                 q.append((r[1], time+r[2], 1))
    #             else:
    #                 q.append((r[1], time