T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    sum = 0
    for i in range(0,10):
        if (N[i]%2) == 1:
            sum += N[i]
        else:
            pass
    print(f"#{tc} {sum}")