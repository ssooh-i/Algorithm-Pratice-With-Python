T = int(input())
for tc in range(1, T+1):
    N = list(map(int, input().split()))
    print(f"#{tc} {round(sum(N)/10)}") #round쓰면 반올림됨