def solution(priorities, location):
    answer = 0
    for i in range(len(priorities)):
        print(priorities[i])
    return priorities


P = [2, 1, 3, 2]
L = 2
print(*solution(P, L))