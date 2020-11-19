def solution(w,h):
    if h>w:
        w, h = h, w
    elif h==w:
        return h*w-h
    return h*w - (((w//h)+1)*h)


print(solution(5,2))
