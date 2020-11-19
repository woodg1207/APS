def solution(w,h):
    if h>w:
        w, h = h, w
    elif h==w:
        return h*w-h
    def new_round(l, r):
        if l%1:
            nl = l//1 + 1
        else:
            nl = l
        if r%1:
            nr = r//1
        else:
            nr = r - 1
        return nr-nl + 2

    diag = w/h
    cnt = 0
    for i in range(h):
        cnt += new_round(diag*i,diag*(i+1))

    return h*w - cnt
print(solution(8,12))
print(solution(5,2))
print(solution(500,2))
