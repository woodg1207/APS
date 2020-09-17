from collections import deque

def solution(progresses, speeds):
    answer = []
    n = len(progresses)
    done = [False] * n 
    q = deque()
    speed = deque()
    release = deque()
    q.extend(progresses)
    speed.extend(speeds)
    release.extend(done)
    while q:
        for i in range(len(q)):
            q[i] += speed[i]
            if q[i]>=100:
                release[i] = True
        if release[0]:
            cnt = 0
            for i in range(len(release)):
                if release[i]:
                    q.popleft()
                    speed.popleft()
                    cnt += 1
                else:
                    break
            for i in range(cnt):
                release.popleft()
            answer.append(cnt)
    return answer


P=[93, 30, 55]
S=[1, 30, 5]
print(solution(P, S))