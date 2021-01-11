def solution(n):
    answer = ''
    l = 3
    cnt = 1
    while n>l:
        cnt += 1
        l += l*3
    n -= 3**(cnt-1)
    for i in range(cnt):
        
    return cnt 


print(solution(13))