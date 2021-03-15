abc = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
numToAbc = dict()
abcToNum = dict()
for i in range(len(abc)):
    numToAbc[i] = abc[i]
    abcToNum[abc[i]] = i

def comb(o, c, idx, cnt):
    if c == cnt:
        print(o[idx])
        return [o[idx]]
    r = [o[idx]]
    for i in range(idx+1, len(o)):
        r.extend(comb(o, c, i, cnt+1))
        r.pop()
    return r

def convertNum(order):
    r = []
    for i in range(len(order)):
        r.append(abcToNum[order[i]])
    return sorted(r)

def solution(orders, course):
    
    answer = []
    for l in course:
        sampleMenu = []
        for order in orders:
            # order = convertNum(order)
            if l > len(order): continue
            sampleMenu.append(comb(order, 3, 0, 1))
            break
        break
    
    return sampleMenu



print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))