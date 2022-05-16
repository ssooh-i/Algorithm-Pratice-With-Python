T = int(input())
for i in range(1, T+1):
    list_t = list(map(int, input().split(" ")))
    if len(list_t) == 10:
        sum_t = 0
        for j in range(0, 10):
            if (list_t[j]%2) == 1:
                sum_t = list_t[j] + sum_t
    print("#"+str(i), sum_t)