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