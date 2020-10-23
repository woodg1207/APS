def solution(N, number):
    memory = [[False for i in range(8)]]*1000000
    def dfs(result, cnt):
        if cnt>8:
            return
        for i in range(5):
            if not i:
                result = int(str(result)+str(N))
                dfs(result, cnt+1)
            elif i==1:
                result += N
                dfs(result, cnt)
            

        return
    return 0

n = 5
Num = 12
# print(solution(n, Num))
from pprint import pprint
r = 0
l = []
for i in range(1,10):
    for j in range(1, 10):
        if i==j:continue
        for k in range(1, 10):
            if i == k or j == k:continue
            r = k*((20*i) + j) + (101*i*j)
            if r > 1000:
                l.append([r, i, j, k])
pprint(l)             