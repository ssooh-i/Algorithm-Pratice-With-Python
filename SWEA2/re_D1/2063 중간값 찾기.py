#다시 풀기
T = int(input())
n = list(map(int, input().split()))
idx = 0
med = 0
if (n % 2) == 1:
    n.sort()
    idx = n // 2
    med = n[idx]
    print(med)


n = int(input())
n_list = list(map(int, input().split(" ")))
idx = 0
med = 0
if 8 < n < 200:
    if (n % 2) == 1:
        n_list.sort()
        idx = n // 2
        med = n_list[idx]
        print(med)
    else:
        print(-2)

else:
    print(-1)