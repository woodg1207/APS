def comb(o, c, cnt):
    for i in range(cnt, len(o)):
        pass        
    return
def solution(orders, course):
    answer = []
    for order in orders:
        for i in course:
            comb(order, i, 0)
    
    return answer



print(solution(["ABCFG", "AC", "CDE", "ACDE", "BCFG", "ACDEH"], [2, 3, 4]))