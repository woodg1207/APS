answer = 0
def solution(numbers, target):
    n = len(numbers)
    temp = 0
    def dfs(n, cnt, temp):
        global answer
        if n==cnt:
            if temp == target:
                answer += 1
            return
        for i in range(2):
            if i:
                temp += numbers[cnt]
                dfs(n,cnt+1, temp)
                temp -= numbers[cnt]
            else:
                temp -= numbers[cnt]
                dfs(n,cnt+1, temp)
                temp += numbers[cnt]
    for i in range(2):
        if i:
            temp += numbers[0]
            dfs(n,1, temp)
            temp -= numbers[0]
        else:
            temp -= numbers[0]
            dfs(n,1, temp)
            temp += numbers[0]

    
    return answer

print(solution([1,1,1,1,1], 3))