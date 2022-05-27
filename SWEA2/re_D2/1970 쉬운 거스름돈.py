T = int(input())
money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
for tc in range(1, T+1):
    N = int(input())
    count = [0 for _ in range(8)]
    print(f"#{tc}")
    for i in range(8):
        if (N// money[i]) > 0:
            count[i] += N//money[i]
            N = N % money[i]
    print(*count)
