def solution(answers):
    answer ={
        '1': [1, 2, 3, 4, 5],
        '2' : [2, 1, 2, 3, 2, 4, 2, 5],
        '3': [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

    }
    point_1 = 0
    point_2 = 0
    point_3 = 0

    for i in range(len(answers)):
        a = i%len(answer['1'])
        if answers[i]==answer['1'][i%len(answer['1'])]:
            point_1+=1
        if answers[i]==answer['2'][i%len(answer['2'])]:
            point_2+=1
        if answers[i]==answer['3'][i%len(answer['3'])]:
            point_3+=1
    l = [point_1,point_2,point_3]
    result = []
    for i in range(3):
        if l[i]==max(l):
            result.append(i+1)
    return result


A =[1,3,2,4,2]
print(solution(A))