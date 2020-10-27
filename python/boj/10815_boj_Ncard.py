import sys; sys.stdin = open('s10815.txt', 'r')

N = int(input())
sang = dict()
for i in input().split():
    sang[i] = 1
M = int(input())
result = []

for i in input().split():
    try:
        result.append(sang[i])
    except:
        result.append(0)
print(*result)