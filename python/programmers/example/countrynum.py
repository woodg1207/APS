def solution(n):
    answer = ''
    l = 3
    cnt = 1
    pre = 1
    while n>l:
        pre = l
        cnt += 1
        num = 3**cnt
        l += num
    if cnt == 1:
        pass
    else:
        for i in range(cnt):
            if i:
                pass
            else:
                n -= pre
                        
                        
    return cnt 


print(solution(13))