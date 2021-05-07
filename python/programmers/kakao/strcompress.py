def solution(s):
    n = len(s)//2
    M = 1001
    for i in range(1, n+1):
        result = ''
        pre = False
        cnt = 1
        for j in range(0, len(s),i):
            if pre == s[j:j+i]:
                cnt += 1
            else:
                if pre:
                    if cnt==1:
                        result += pre
                    else:
                        result += str(cnt)+pre
                    cnt = 1
            pre = s[j:j+i]
        if cnt == 1:
            result += pre
        else:
            result += str(cnt)+pre
        if len(result) < M:
            M = len(result)
    if M >len(s):
        M = len(s)
    return M

print(solution('aabbaccc'))
print(solution('ababcdcdababcdcd'))
print(solution('abcabcdede'))
print(solution('abcabcabcabcdededededede'))
print(solution('xababcdcdababcdcd'))