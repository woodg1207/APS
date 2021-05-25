def solution(t, r):
    answer = []
    hold = []
    for i in range(len(t)):
        hold.append((i, t[i], r[i]))
    hold.sort(key=lambda x: x[1])
    for i in range(10001):
        temp=[]
        if i < hold[0][1]:continue
        for j in range(len(hold)):
            if i >= hold[j][1]:
                temp.append(hold[j])
        if len(temp):
            temp = sorted(temp, key=lambda x:x[2])
            cnt = []
            for i in temp:
                if temp[0][2] == i[2]:
                    cnt.append(i)
            if len(cnt) != 1:
                cnt.sort(key=lambda x:x[0])
                temp = cnt[0]
            hold.pop(hold.index(temp[0]))
            answer.append(temp[0])
        if not hold:
            break
    r = [0]*len(r)
    for i in range(len(answer)):
        r[i] = answer[i][0]
    return r


print(solution([7,6,9999,1],[0,1,2,3]	))
# print(solution([0,1,3,0], [0,1,2,3]))