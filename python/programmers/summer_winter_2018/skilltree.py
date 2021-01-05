eng = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
eng_dict = dict()
num_dict = dict()
for i in range(26):
    eng_dict[i] = eng[i]
    num_dict[eng[i]] = i
def solution(skill, skill_trees):
    priority = [0]*26
    answer = 0
    for i in range(len(skill)):
        priority[num_dict[skill[i]]] = i+1
    for skill_tree in skill_trees:
        cnt = 0
        flag = 0
        for s in skill_tree:
            if priority[num_dict[s]]:
                if priority[num_dict[s]] - cnt == 1:
                    cnt += 1
                else:
                    flag = 1
            if flag:
                break
        if flag:
            continue
        else:
            answer += 1
            
    return answer

print(solution("CBD",["BACDE", "CBADF", "AECB", "BDA"]))