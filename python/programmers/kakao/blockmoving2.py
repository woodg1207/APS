from pprint import pprint
from collections import deque

def direction(r):
    if r[0][1]==r[1][0]:
        return 1 # 가로
    return 0 # 세로

def spinCheck(r, n, d, b):
    if d: # 가로
        if b[n[0]][r[0][1]] or b[n[0]][r[1][1]]: return 0
    else:
        if b[r[0][0]][n[1]] or b[r[1][0]][n[1]]: return 0
    return 1
    
def destinationCheck(r, n):
    for i in range(2):
        if r[i] == [n-1, n-1]:
            return 1
    return 0

def solution(board):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    answer = 0
    N = len(board)    
    visit = [[[False for _ in range(N)] for _ in range(N)] for _ in range(2)]
    robot = [[0,0], [0,1], 0]
    q = deque()
    q.append(robot)
    while q:
        r = q.popleft()
        # print(q)
        # print(r)
        if destinationCheck(r, N):
            # print(r)
            answer = r[-1]
            break
        d = direction(r)
        for i in range(2):
            visit[0][r[i][0]][r[i][1]]=True
            visit[1][r[i][0]][r[i][1]]=True

        for i in range(2):
            for j in range(4):
                nr, nc = r[i][0]+dr[j], r[i][1]+dc[j]
                if 0<=nr<N and 0<=nc<N:
                    if [nr, nc] == r[0] or [nr, nc] == r[1]: continue
                    elif board[nr][nc]: continue
                    if d:# 가로의 경우
                        if r[i][0]!=nr:
                            if not spinCheck(r, [nr, nc], d, board): continue
                    else:
                        if r[i][1] != nc:
                            if not spinCheck(r, [nr, nc], d, board): continue
                    nd = direction([[r[i][0], r[i][1]],[nr, nc]])
                    if visit[nd][r[i][0]][r[i][1]] and visit[nd][nr][nc]: continue
                    q.append([r[i], [nr, nc], r[2]+1])
                    visit[nd][nr][nc] = True
    # pprint(visit)
    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))
print(solution([[0, 0, 0],[0, 0, 0],[0, 0, 0]]))
# print(solution([
#     [0, 0, 1, 0],
#     [0, 0, 1, 0],
#     [0, 1, 0, 0],
#     [0, 0, 0, 0]
#     ]))