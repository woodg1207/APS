def solution(n, delivery):
    visit = [0] * (n+1)
    for i in range(len(delivery)):
        if delivery[i][2]:
            visit[delivery[i][0]] = 1
            visit[delivery[i][1]] = 1
    for i in range(len(delivery)):
        if not delivery[i][2]:
            flag = 0
            if visit[delivery[i][0]]==1:
                visit[delivery[i][1]] = 2
            elif visit[delivery[i][1]]==1:
                visit[delivery[i][0]] = 2                                                    
    result = ''
    for i in range(1, n+1):
        if visit[i] == 0:
            result += '?'
        elif visit[i] == 1:
            result += 'O'
        elif visit[i] == 2:
            result += 'X'


    return result

N = 6
D = [[1,3,1],[3,5,0],[5,4,0],[2,5,0]]
print(solution(N, D))