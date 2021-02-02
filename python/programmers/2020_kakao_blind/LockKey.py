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

def solution(key, lock):
    N = len(lock)
    M = len(key)
    for r in range(4):
        k = rotate(key, r, 0)
        ## 위치이동 시키면서 맞추기.
        for i in range(N):
            for j in range(N):
                pass

    return 0

print(solution(
    [[0, 0, 0], [1, 0, 0], [0, 1, 1]], 
    [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    ))