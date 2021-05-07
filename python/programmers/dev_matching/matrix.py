from pprint import pprint
from collections import deque
def make_arr(r, c):
    n = r*c
    cnt = 1
    result = []
    for i in range(r):
        temp = []
        for j in range(c):
            temp.append(cnt)
            cnt += 1
        result.append(temp)
    return result

def make_list(x1, y1, x2, y2):
    result = []
    for i in range(y1, y2+1):
        result.append((x1, i))
    for i in range(x1+1, x2+1):
        result.append((i, y2))
    for i in range(y2-1, y1-1, -1):
        result.append((x2, i))
    for i in range(x2-1, x1, -1):
        result.append((i, y1))
    return result

def change_num(l, arr):
    q = deque()
    q.extend(l)
    n = q.pop()
    q.appendleft(n)
    result = []
    for i in range(len(l)):
        r, c = q[i]
        result.append(arr[r][c])
    return result, min(result)

def solution(rows, columns, queries):
    N = len(queries)
    arr = make_arr(rows, columns)
    answer = []
    for i in range(N):
        x1, y1, x2, y2 = queries[i]
        x1, y1, x2, y2 = x1-1, y1-1, x2-1, y2-1
        lst = make_list(x1, y1, x2, y2)
        n_lst, m = change_num(lst, arr)
        for j in range(len(lst)):
            arr[lst[j][0]][lst[j][1]] = n_lst[j]
        answer.append(m)
    return answer



r, c, q = 6, 6, [[2,2,5,4],[3,3,6,6],[5,1,6,3]]
print(solution(r, c, q))