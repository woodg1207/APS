# def comb(depth, l):
#     result = []
#     cnt = 1:
#     while depth > cnt:
#         if not result:
#             for i in range(len(l)):
#                 result.append([i])
#         else:
#             for i in range(len(result)):
#                 for j in range(i+1, len(l)):



#         cnt += 1

#     return
# def comb(lst,n):
# 	ret = []
# 	if n > len(lst): return ret
	
# 	if n == 1:
# 		for i in lst:
# 			ret.append([i])
# 	elif n>1:
# 		for i in range(len(lst)-n+1):
# 		    for temp in comb(lst[i+1:],n-1):
# 			    ret.append([lst[i]]+temp)

# 	return ret
from copy import deepcopy, copy
def comb(l, n):
    result = []
    def dfs(idx, n, cnt):
        if cnt == n:
            x = temp[:]
            result.append(x)
            return
        for i in range(idx+1, len(l)):
            temp.append(l[i])
            dfs(i, n, cnt+1)
            temp.pop()
        return

    for i in range(len(l)):
        temp = [l[i]]
        dfs(i, n, 1)
    return result


test = ['a', 'b', 'c', 'd', 'e']
depth = 3
print(comb(test, depth))
