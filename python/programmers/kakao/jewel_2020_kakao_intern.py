def solution(gems):
    visit = list(set(gems))
    m = len(gems)+1
    for i in range(len(gems)-len(visit)+1):
        visit_bool = [1]*(len(visit))
        visit_bool[visit.index(gems[i])] = 0
        start = i
        while sum(visit_bool) != 0:
            i += 1
            if i-start > m:
                break
            if i<len(gems): 
                if visit_bool[visit.index(gems[i])]:
                    visit_bool[visit.index(gems[i])] = 0
            else:
                break
        else:
            end = i
            if (end-start)<m:
                m = end-start
                result = [start+1, end+1]
    return result


G = ["DIA", "RUBY", "RUBY", "DIA", "DIA", "EMERALD", "SAPPHIRE", "DIA"]
print(solution(G))