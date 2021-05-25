from itertools import permutations
def make_num(num):
    result = []
    visit = [False]*10000000
    l = []
    for n in range(1, len(num)+1):
        result.extend(permutations(num, n))
    for i in range(len(result)):
        temp = ''
        for j in range(len(result[i])):
            if j==0 and result[i][j]=='0':
                continue
            temp += result[i][j]
        if not temp: continue
        temp_num = int(temp)
        if visit[temp_num]:
            continue
        visit[temp_num] = True
        l.append(temp_num)
    return l

def check_decimal(l):
    result = []
    for num in l:
        if num<2: continue
        for i in range(2, num):
            if num%i == 0:
                break
        else:
            result.append(num)
    print(result)
    return len(result)
def solution(numbers):
    return check_decimal(make_num(numbers))


print(solution('011'))