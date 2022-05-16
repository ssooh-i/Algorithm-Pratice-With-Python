P, K = list(map(int, input().split()))
n = 0
re = 0
for i in range(K, P+1):
    Ke = K + 1
    n = i
    re = n - K + 1
print(re)