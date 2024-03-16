# 백준 1546
n = int(input())
a = list(map(int, input().split()))
max = 0

# 최대값 찾기
for i in a:
    if max < i:
        max = i

# 새로운 점수 구하기
new_sum = 0
for i in a:
    new_sum += (i/max)*100

print(new_sum/n)