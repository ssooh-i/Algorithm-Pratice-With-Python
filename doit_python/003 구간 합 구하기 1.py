# 백준 11659번
n = int(input())
m = int(input())

list_a = list(map(int, input().split()))

list_b = [m][2]

for i in range(len(n)-1):
    for j in range(len(n)):
