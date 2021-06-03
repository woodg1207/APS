def solution(n, lost, reserve):
    res_lst = [False] * (n+1)    
    res_lst2 = [False] * (n+1)    
    lost.sort()
    for i in reserve:
        res_lst[i] = True
        res_lst2[i] = True
    cnt = n-len(lost)
    cnt2 = n-len(lost)
    while lost:
        student = lost.pop()
        if res_lst[student-1]:
            res_lst[student-1] = False
            cnt += 1
        elif student!=n and res_lst[student+1]:
            res_lst[student+1] = False
            cnt += 1
        if student!=n and res_lst2[student+1]:
            res_lst2[student+1] = False
            cnt2 += 1
        elif res_lst2[student-1]:
            res_lst2[student-1] = False
            cnt2 += 1
    if cnt>cnt2:
        return cnt
    return cnt2

N = 5
L = [2, 4]
R = [3, 1, 5]
print(solution(N, L, R))