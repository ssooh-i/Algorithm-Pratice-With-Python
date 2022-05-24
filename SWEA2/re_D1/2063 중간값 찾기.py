T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    n = N.sort()
    idx = n // 2
    med = N[idx]
    print(f"#{tc} {med}")

