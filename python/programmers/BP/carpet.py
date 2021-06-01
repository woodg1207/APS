def solution(brown, yellow):
    answer = []
    if yellow==1:
        return [3,3]
        
    for column in range(1,yellow//2+1):
        if yellow%column==0:
            r = yellow//column
            if brown == (r*2) + (column*2) +4:
                break
    
    return [r+2, column+2]

print(solution(10, 2))