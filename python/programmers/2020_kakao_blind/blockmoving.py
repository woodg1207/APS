from pprint import pprint
from collections import deque

def direction(r):
    if r[0][1]==r[1][0]:
        return 1 # 가로
    return 0 # 세로

def spinCheck(r, n):
    for i in range(2):
        if i:
            pass
        else:
            pass
    return
    
def solution(board):
    dr = [1, 0, -1, 0]
    dc = [0, 1, 0, -1]
    answer = 0
    N = len(board)    
    visit = [[False for _ in range(N)] for _ in range(N)]
    robot = [[0,0], [0,1]]
    q = deque()
    q.append(robot)
    while q:
        r = q.popleft()
        d = direction(r)
        for i in range(2):
            for j in range(4):
                nr, nc = r[i][0]+dr[j], r[i][1]+dc[j]
                if 0<=nr<N and 0<=nc<N:
                    if [nr, nc] == r[0] or [nr, nc] == r[1]: continue
                    elif visit[nr][nc]: continue
                    if d:# 가로의 경우
                        if r[i][0]==nr:
                            if board[nr][nc]: continue
                        else:
                            spinCheck(r,[nr, nc])
                    else:
                        pass

    return answer


print(solution([[0, 0, 0, 1, 1],[0, 0, 0, 1, 0],[0, 1, 0, 1, 1],[1, 1, 0, 0, 1],[0, 0, 0, 0, 0]]))