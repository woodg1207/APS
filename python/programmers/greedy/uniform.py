def solution(n, lost, reserve):
    cnt = 0
    reserve = sorted(reserve)
    for i in range(len(lost)):
        flag = 0
        for j in range(len(reserve)):
            if -1 <= lost[i]-reserve[j] <= 1:
                reserve.pop(j)
                flag = 1
                break
        if flag:
            cnt += 1
    return n-len(lost)+cnt

N = 5
L = [2, 4]
R = [3, 1, 5]
print(solution(N, L, R))