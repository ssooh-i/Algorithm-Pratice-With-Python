T = int(input())
A = ['4','6','9','11']
for tc in range(1, T+1):
    day = input()
    y = day[:4]
    m = day[4:6]
    d = day[6:]
    print(f"#{tc} ", end="")
    if ((0<int(m)<13) & (0<int(d)<32)) & (int(m) != 2):
        if m in A:
            if int(d) < 31:
                print(f"{y}/{m}/{d}")
            else:
                print(-1)
        else:
            if int(d) < 32:
                print(f"{y}/{m}/{d}")
    elif int(m) == 2:
        if (0 < int(d) < 29):
            print(f"{y}/{m}/{d}")
        else:
            print(-1)
    else:
        print(-1)
