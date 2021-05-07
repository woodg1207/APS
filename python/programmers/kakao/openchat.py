def solution(record):
    answer = []
    userid = []
    info = dict()
    for i in range(len(record)):
        temp_str = ''
        if len(record[i].split())==3:
            verb, uid, name = record[i].split()
        else:
            verb, uid = record[i].split()
        if verb == 'Leave':
            temp_str += '님이 나갔습니다.'
        else:
            info[uid] = name
            if verb == 'Enter':
                temp_str += '님이 들어왔습니다.'
        if temp_str:
            answer.append(temp_str)
            userid.append(uid)
    for i in range(len(answer)):
        answer[i] = info[userid[i]]+answer[i]
    return answer


r = ["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
print(solution(r))