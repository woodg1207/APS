def solution(encrypted_text, key, rotation):
    x = 'abcdefghijklmnopqrstuvwxyz'
    e = []
    k = []
    abc = dict()
    num = dict()
    for i in range(26):
        abc[x[i]] = i+1
        num[i+1] = x[i]
    flag = 0
    if rotation > 0 :
        flag = 1  # 왼쪽으로 이동
    s = ''
    if flag: 
        s = encrypted_text[rotation:] + encrypted_text[:rotation]
    else:
        rotation += len(key)
        s = encrypted_text[rotation:] + encrypted_text[:rotation]
    
    encrypted_text = s
    for i in range(len(key)):
        e.append(abc[encrypted_text[i]])
        k.append(abc[key[i]])
    for i in range(len(key)):
        e[i] -= k[i]
    result = ''
    for i in range(len(e)):
        x = e[i]%26
        if not x:
            x = 26
        result += num[x]
    return result


E = 'qyyigoptvfb'
K = 'abcdefghijk'
R = 3
print(solution(E, K, R))