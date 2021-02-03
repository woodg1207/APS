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

def delete_p(x, y, w):
    # if w.get()
    return

def delete_b(x, y, w):
    return

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
        if b: # create
            if a: # 1 = bo
                if create_b(x, y, wall):
                    wall['{}{}1'.format(x, y)] = 1
            else: # call pillar create
                if create_p(x, y, wall):
                    wall['{}{}0'.format(x, y)] = 1
        else: # delete
            if a:
                pass
            else:
                pass
    
    return convert(wall)

print(solution(5, [[1,0,0,1],[1,1,1,1],[2,1,0,1],[2,2,1,1],[5,0,0,1],[5,1,0,1],[4,2,1,1],[3,2,1,1]]))