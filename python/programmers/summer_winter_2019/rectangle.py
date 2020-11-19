def solution(w,h):
    if h>w:
        w, h = h, w
    elif h==w:
        return h*w-h
    def new_round(num):
        if num == 0:
            return 0 
        if num % 1:
            return num//1
        else:
            return num - 1
    diag = w/h
    cnt = 0
    for i in range(h):
        cnt += new_round(diag*(i+1))-new_round(diag*i) + 1
        print(new_round(diag*(i+1)),new_round(diag*i), cnt)
    return h*w - cnt
print(solution(8,12))
# print(solution(5,2))
# print(solution(500,2))
