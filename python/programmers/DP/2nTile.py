def solution(n):
    l = [1, 2]
    for i in range(2, n):
        l.append((l[i-2]+l[i-1])%1000000007)
    return l[-1]


print(solution(4))