from collections import deque
def solution(priorities, location):
    cnt = 0
    printer = deque()
    important = [0]*10
    for i in range(len(priorities)):
        important[priorities[i]] += 1
        if i == location:
            printer.append((priorities[i], 1))
        else:
            printer.append((priorities[i], 0))
    c = 0
    while 1:
        c += 1
        flag = 0
        paper = printer.popleft()
        for i in range(paper[0]+1,10):
            if important[i]>0:
                flag = 1
                break
        if flag:
            printer.append(paper)
        else:
            cnt += 1
            important[paper[0]] -= 1
            if paper[1]:
                break
        # print(printer, paper)
        # print(important)
        # if c == 8:
        #     break
    return cnt


P = [2, 1, 3, 2]
L = 2
print(solution(P, L))