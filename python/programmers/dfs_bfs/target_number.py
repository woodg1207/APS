def solution(numbers, target):
    n = len(numbers)
    answer = []
    temp = 0
    def dfs(n, cnt, temp):
        if n==cnt:
            if temp == target:
                answer.append(1)
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

    
    return len(answer)

print(solution([1,1,1,1,1], 3))