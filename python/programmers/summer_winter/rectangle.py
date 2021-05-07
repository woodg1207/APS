def solution(w,h):
    if h>w:
        w, h = h, w
    elif h==w:
        return h*w-h
    def new_round(l, r):
        nl, nr = l//1, r//1
        if r%1 == 0:
            nr -= 1
        return nr - nl + 1

    diag = w/h
    cnt = 0
    for i in range(h):
        if (diag*i) % 1 == 0 and i != 0:
            break
        cnt += new_round(diag*i,diag*(i+1))
    
    if h-i == 1:
        i = h
    cnt *= (h//i)
    return h*w - cnt
print(solution(8,12))
print(solution(5,2))
print(solution(54044490,143333340))
