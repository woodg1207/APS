def create_p(x, y, w):
    if y == 0:
        # w['{}{}0'.format(x,y)] = 1
        return 1
    else:
        if w.get('{}{}0'.format(x,y-1)) or w.get('{}{}1'.format(x-1,y)) or w.get('{}{}1'.format(x, y)):
            return 1
        return 0

def create_b(x, y, w):
    if w.get('{}{}0'.format(x, y-1)) or w.get('{}{}0'.format(x+1, y-1)) or (w.get('{}{}1'.format(x-1,y)) and w.get('{}{}1'.format(x+1,y))):
        return 1
    return 0 

def delete(x, y, z, l):
    ## 기록들을 통해서 순서대로 만드는데 특정 기록은 스킵하고 
    # 만들때 한곳이라도 만들수 없으면 못만드는것을 리턴해주도록 만들기
    w = dict()
    for i in range(len(l)):
        if [x, y, z] == l[i]:
            continue
        if l[i][2]:
            if not create_b(l[i][0], l[i][1], w):
                return 1
            w['{}{}1'.format(l[i][0], l[i][1])] = 1
        else:
            if not create_p(l[i][0], l[i][1], w):
                return 1
            w['{}{}0'.format(l[i][0], l[i][1])] = 1
    return 0


def convert(w):
    result = []
    for k, v in w.items():
        if v:
            result.append([int(k[0]), int(k[1]), int(k[2])])
    return sorted(result, key=lambda x : (x[0], x[1], x[2]))

def solution(n, build_frame):
    wall = dict()
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        sample = []
        if b: # create
            if a: # 1 = bo
                if create_b(x, y, wall):
                    wall['{}{}1'.format(x, y)] = 1
                    sample.append([x, y, 1])
            else: # call pillar create
                if create_p(x, y, wall):
                    wall['{}{}0'.format(x, y)] = 1
                    sample.append([x, y, 0])
        else: # delete
            if delete(x, y, a, sample):
                wall['{}{}{}'.format(x, y, a)] = 0
                temp = []
                for idx in range(len(sample)):
                    if [x, y, a] == sample[idx]: continue
                    temp.append(sample[idx])
                sample = temp
    return convert(wall)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))