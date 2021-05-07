def check(w):
    x = 0
    if not len(w): return ''
    for i in range(len(w)):
        #균형이 잡히면 자르기. 
        if w[i] == '(': x += 1
        else: x -= 1
        if x == 0:
            u, v = w[:i+1], w[i+1:]
            break
    # u가 올바른지 확인.
    # print(u,'   ', v)
    for i in range(len(u)):
        if u[i] == '(': x += 1
        else: x -= 1
        if x<0:
            break
    else:
        # 올바른 u
        return u + check(v)
    # 이상한 u
    temp = ''
    for br in u[1:len(u)-1]:
        if br == '(': temp += ')'
        else: temp += '('
    
    return '('+ check(v) + ')' + temp
def solution(p):
    return check(p)

print(solution('(()())()'))
print(solution(')('))
print(solution('()))((()'))
