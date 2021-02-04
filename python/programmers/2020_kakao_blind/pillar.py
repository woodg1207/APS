from pprint import pprint
def create_p(x, y, w):
    if y == 0:
        return 1
    else:
        if w.get('{}{}0'.format(x,y-1)) or w.get('{}{}1'.format(x-1,y)) or w.get('{}{}1'.format(x, y)):
            return 1
        return 0

def create_b(x, y, w):
    if w.get('{}{}0'.format(x, y-1)) or w.get('{}{}0'.format(x+1, y-1)) or (w.get('{}{}1'.format(x-1,y)) and w.get('{}{}1'.format(x+1,y))):
        return 1
    return 0 

def delete(x, y, a, w):
    if w.get('{}{}{}'.format(x, y, a)):
        w['{}{}{}'.format(x, y, a)] = 0
    else:
        return 1
    if a: #bo
        if w.get('{}{}{}'.format(x-1, y, 1)):
            if not create_b(x-1, y, w):
                return 0
        if w.get('{}{}{}'.format(x, y, 0)):
            if not create_p(x, y, w):
                return 0
        if w.get('{}{}{}'.format(x+1, y, 1)):
            if not create_b(x+1, y, w):
                return 0
        if w.get('{}{}{}'.format(x+1, y, 0)):
            if not create_p(x+1, y, w):
                return 0
    else:
        if w.get('{}{}{}'.format(x+1,y+1,1)):
            if not create_b(x+1, y+1, w):
                return 0
        if w.get('{}{}{}'.format(x,y+1,0)):
            if not create_p(x, y+1, w):
                return 0
        if w.get('{}{}{}'.format(x,y+1,1)):
            if not create_b(x, y+1, w):
                return 0
    return 1


def convert(w):
    result = []
    for k, v in w.items():
        if v:
            result.append([int(k[0]), int(k[1]), int(k[2])])
    return sorted(result, key=lambda x : (x[0], x[1], x[2]))

def solution(n, build_frame):
    wall = dict()
    sample = []
    for i in range(len(build_frame)):
        x, y, a, b = build_frame[i]
        if b: # create
            if a: # 1 = bo
                if create_b(x, y, wall):
                    wall['{}{}1'.format(x, y)] = 1
            else: # call pillar create
                if create_p(x, y, wall):
                    wall['{}{}0'.format(x, y)] = 1
        else: # delete b = 0
            if delete(x, y, a, wall):
                wall['{}{}{}'.format(x, y, a)] = 0
            else:
                print(wall, '@@')
                wall['{}{}{}'.format(x, y, a)] = 1
            print(wall, (x, y, a), '##') 
    return convert(wall)


print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))
print(solution(5, [[0,0,0,1],[2,0,0,1],[4,0,0,1],[0,1,1,1],[1,1,1,1],[2,1,1,1],[3,1,1,1],[2,0,0,0],[1,1,1,0],[2,2,0,1]]))