from collections import deque

dr=[1,0,-1,0]
dc=[0,1,0,-1]
def manh(r, c, nr, nc):
    if abs(r-nr)+abs(c-nc)>2:
        return 1
    else:
        return 0
def solution(places):
    answer = []
    for room in places:
        visit = [[False]*5 for _ in range(5)]
        flag = 0
        for i in range(5):
            for j in range(5):
                if room[i][j] == 'P':
                    q = deque()
                    q.append((i,j))
                    visit[i][j]= True
                    while q:
                        r, c = q.popleft()
                        for n in range(4):
                            nr, nc = r+dr[n], c+dc[n]
                            if 0<=nr<5 and 0<=nc<5:
                                if visit[nr][nc]: continue
                                if room[nr][nc]=='X':
                                    continue
                                if manh(i, j, nr, nc):
                                    continue
                                if room[nr][nc]=='P':
                                    flag = 1
                                    break
                                else:
                                    q.append((nr, nc))
                                    visit[nr][nc] = True
                        if flag:
                            answer.append(0)
                            break
                if flag: break
            if flag: break
        if not flag:
            answer.append(1)


    return answer


print(solution([["POOOP", "OXXOX", "OPXPX", "OOXOX", "POXXP"], ["POOPX", "OXPXP", "PXXXO", "OXXXO", "OOOPP"], ["PXOPX", "OXOXP", "OXPXX", "OXXXP", "POOXX"], ["OOOXX", "XOOOX", "OOOXX", "OXOOX", "OOOOO"], ["PXPXP", "XPXPX", "PXPXP", "XPXPX", "PXPXP"]]))