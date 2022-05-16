T = int(input())
max_n = 0
for i in range(1, T+1):
    list_n = list(map(int, input().split(" ")))
    max_n = max(list_n)
    print("#"+str(i), max_n)