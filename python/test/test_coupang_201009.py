def solution(v):
    r_list = []
    c_list = []
    r, c = 0, 0 
    for i in v:
        r_list.append(i[0])
        c_list.append(i[1])
    
    sample = [r_list.pop(), c_list.pop()] 
    if sample[0] in r_list:
        for i in range(2):
            if r_list[i] != sample[0]:
                r = r_list[i]
                break
    else:
        r = sample[0]
    
    if sample[1] in c_list:
        for i in range(2):
            if c_list[i] != sample[1]:
                c = c_list[i]
                break
    else:
        c = sample[1]

    return [r, c]

V=[[1, 1], [2, 2], [1, 2]]
print(solution(V))