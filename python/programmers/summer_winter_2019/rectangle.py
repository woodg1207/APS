def solution(w,h):
    answer = 1
    for i in range(w):
        answer += i
    return answer


print(solution(8,12))
