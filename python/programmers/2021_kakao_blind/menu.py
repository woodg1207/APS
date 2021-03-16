from copy import deepcopy
def comb(l, n):
    result = []
    def dfs(idx, n, cnt):
        if cnt == n:
            x = deepcopy(temp)
            result.append(x)
            return
        for i in range(idx+1, len(l)):
            temp.append(l[i])
            dfs(i, n, cnt+1)
            temp.pop()
        return
    for i in range(len(l)):
        temp = [l[i]]
        dfs(i, n, 1)
    return result

def convert(order):
    eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    try:
        int(order[0])
    except:
        temp = []
        for word in order:
            temp.append(eng.index(word))
        temp = sorted(temp)
    else:
        temp = ''
        for i in order:
            temp+=eng[i]
    return temp

def solution(orders, course):
    answer = []
    for l in course:
        sampleMenu = []
        M = 1
        temp = []
        for order in orders:
            order = convert(order)
            if l > len(order): continue
            sampleMenu.append(comb(order,l))
        for menus in range(len(sampleMenu)-1):
            for menu in range(len(sampleMenu[menus])):
                cnt = 1
                for targets in range(menus+1, len(sampleMenu)):
                    for target in range(len(sampleMenu[targets])):
                        if sampleMenu[menus][menu] == sampleMenu[targets][target]:
                            cnt += 1
                
                if cnt>M:
                    temp = [sampleMenu[menus][menu]]
                    M = cnt
                elif M==cnt and cnt != 1:
                    if sampleMenu[menus][menu] in temp: continue
                    temp.append(sampleMenu[menus][menu])
        answer.extend(sorted(temp))
    result = [convert(i) for i in answer]

    return result



print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))
print(solution(["XYZ", "XWY", "WXA"],[2,3,4]))