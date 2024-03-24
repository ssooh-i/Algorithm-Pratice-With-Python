# 백준 11660번
# 표의 크기 n (n*n배열준비), 합을 구해야하는 횟수 m
# 표에 삽입할 데이터 (0부터 아니고 1부터 인덱스 생각해주기)
# m개의 줄에 x1 y1 x2 y2가 주어짐
# x1 y1부터 x2,y2까지의 합 구하기

import sys

input = sys.stdin.readline
n, m = map(int, input().split())
mapA = [[0] * (n+1)]
mapD = [[0] * (n+1) for _ in range(n+1)]

for i in range(n):
    mapA_row = [0] + [int(x) for x in input().split()]
    mapA.append(mapA_row)
for i in range(1, n+1):
    for j in range(1, n+1):
        mapD[i][j] = mapD[i][j - 1] + mapD[i - 1][j] - mapD[i - 1][j - 1] + mapA[i][j]

for _ in range(m):
    X1, Y1, X2, Y2 = map(int, input().split())
    result = mapD[X2][Y2] - mapD[X1 - 1][Y2] - mapD[X2][Y1 - 1] + mapD[X1 - 1][Y1 - 1]
    print(result)