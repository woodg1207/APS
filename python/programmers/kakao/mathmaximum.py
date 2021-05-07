from itertools import permutations
def conver_lst(e):
    cal = '*+-'
    temp = ''
    result = []
    for i in e:
        if i in cal:
            result.append(int(temp))
            temp = ''
            result.append(i)
        else:
            temp += i
    else:
        result.append(int(temp))
    return result

def make_postfix(e, p):
    oper = []
    post = []
    for i in e:
        if type(i) is int:
            post.append(i)
        else:
            if i == p[2]:
                while oper and oper[-1]==p[2]:
                    post.append(oper.pop())
                oper.append(i)
            elif i==p[1]:
                while oper and oper[-1]==p[1]:
                    post.append(oper.pop())
                oper.append(i)
            else:
                while oper:
                    post.append(oper.pop())
                oper.append(i)
    while oper:
        post.append(oper.pop())

    return post

def calcul(l):
    result = []
    for i in l:
        if type(i) is int:
            result.append(i)
        elif i=='*':
            t1 = result.pop()
            t2 = result.pop()
            result.append(t1*t2)
        elif i=='+':
            t1 = result.pop()
            t2 = result.pop()
            result.append(t1+t2)
        elif i=='-':
            t1 = result.pop()
            t2 = result.pop()
            result.append(t2-t1)
    return result[-1]

def solution(expression):
    M = 0
    cal = '*+-'
    exp = conver_lst(expression)
    priors = list(permutations(cal, 3))
    for i in range(len(priors)):
        post = make_postfix(exp, priors[i])
        m = calcul(post)
        if M<abs(m):
            M=abs(m)
    return M



exp = "100-200*300-500+20"
print(solution(exp))

# print(make_postfix([1,'-',3,'-',5,'*',5],('-','*')))
print(make_postfix([1,'-',3,'*',5,'-',5],('-','+','*')))
print(calcul(make_postfix([1,'-',3,'*',5,'-',5],('-','+','*'))))
print(calcul([1,3,5,'*','-',5,'-']))