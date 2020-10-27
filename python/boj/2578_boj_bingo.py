import sys; sys.stdin = open('s2578.txt', 'r')

arr = []
speak = []
for i in range(10):
    if i<5:
        arr.append(list(map(int, input().split())))
    else:
        speak.extend(list(map(int, input().split())))
for b in range(25):
    flag = 0
    for i in range(5):
        for j in range(5):
            if arr[i][j] == speak[b]:
                arr[i][j] = 0
                flag = 1
                break
        if flag:
            break
    if b>3:
        bingo = 0
        dia1, dia2 = 0, 0
        # bingo check
        for i in range(5):
            if sum(arr[i]) == 0:
                bingo += 1
            c = arr[0][i] + arr[1][i] + arr[2][i] + arr[3][i] + arr[4][i]
            if not c:
                bingo += 1
            dia1 += arr[i][i]
            dia2 += arr[i][4-i]
        if not dia1: bingo += 1
        if not dia2: bingo += 1
        if bingo >= 3:
            print(b+1)
            break