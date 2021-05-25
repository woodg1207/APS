from datetime import datetime

def solution(code, day, data):
    answer = []
    temp = []
    for d in data:
        p, c, t = d.split()
        p = p.split('=')[-1]
        c = c.split('=')[-1]
        t = t.split('=')[-1]
        if c == code:
            y, m, d, h = t[:4],t[4:6], t[6:8],t[8:]
            if y+m+d == day:
                temp.append((p, datetime(year=int(y), month=int(m), day=int(d), hour=int(h))))
    temp.sort(key=lambda x: x[1])
    
    return [int(i[0]) for i in temp]


print(solution("012345", "20190620",["price=80 code=987654 time=2019062113","price=90 code=012345 time=2019062014","price=120 code=987654 time=2019062010","price=110 code=012345 time=2019062009","price=95 code=012345 time=2019062111"]))