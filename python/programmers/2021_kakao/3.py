from collections import deque

def solution(n, k, cmd):
    answer = ''
    q = deque()
    q.extend([str(i) for i in range(n)])
    delete = []
    for c in cmd:
        if c[0]=='D':
            move = int(c.split()[-1])
            k += move
        elif c[0] == 'U':
            move = int(c.split()[-1])
            k -= move
        elif c[0] == 'C':
            temp = []
            for i in range(k):
                # if len(q) == 0: continue
                temp.append(q.popleft())
            delete.append(q.popleft())
            if temp:
                q.extendleft(temp[::-1])
            if len(q)<=k:
                k = len(q)-1
        else:
            temp = []
            dk = delete.pop()
            i = 0
            while 1:
                if len(q)==0:
                    q.append(dk)
                    break
                if int(q[0])>int(dk):
                    q.appendleft(dk)
                    break
                temp.append(q.popleft())
            if temp:
                q.extendleft(temp[::-1])
            if len(temp)+1<=k:
                k+=1
        # print(q, c, delete, k)

    delete = sorted(delete)[::-1]
    for i in range(n):
        if delete and i == int(delete[-1]):
            answer += 'X'
            if delete:
                delete.pop()
            continue
        answer += 'O'
    return answer



print(solution(8, 2,["D 2","C","U 3","C","D 4","C","U 2","Z","Z","U 1","C"]))