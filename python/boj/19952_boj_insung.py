import sys; sys.stdin = open('s19952.txt', 'r')
from pprint import pprint

tcs = int(input())
dr = [1, 0, -1, 0]
dc = [0, 1, 0, -1]
for tc in range(tcs):
    H, W, O, F, Rs, Cs, Re, Ce = map(int, input().split())
    arr = [[0]*W for _ in range(H)]
    for i in range(O):
        x, y, l = map(int, input().split())
        arr[x-1][y-1] = l
    