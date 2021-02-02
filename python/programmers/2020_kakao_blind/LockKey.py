def rotate(arr, c, cnt):
    if c == cnt: 
        return arr
    n = len(arr)
    result = []
    for i in range(n):
        temp = []
        for j in range(n):
            temp.append(arr[n-j-1][i])
        result.append(temp)
    return rotate(result, c, cnt+1)

def moveCheck(mr, mc, k, l):
    N, M = len(l), len(k)
    for i in range(N):
        for j in range(N):
            x = l[i][j]
            if 0 <= i-mr < M and 0 <= j-mc < M:
                x += k[i-mr][j-mc]
            if x!=1: return False
            
    return True

def solution(key, lock):
    N = len(lock)
    for r in range(4):
        k = rotate(key, r, 0)
        ## 위치이동 시키면서 맞추기.
        for mr in range(-N+1, N):
            for mc in range(-N+1,N):
                if moveCheck(mr, mc, k, lock): return True
    return False

print(solution(
    [[0, 0, 0], [1, 0, 0], [0, 1, 1]], 
    [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    ))
# print(solution(
#     [[1, 1, 1], [1, 1, 0], [1, 0, 1]],
#     [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
#     ))