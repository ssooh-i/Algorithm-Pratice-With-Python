T = int(input())
for tc in range(1, T+1):
    P, Q, R, S, W = map(int, input().split())
    A_price = W * P
    if R < W:
        B_price = Q + ((W-R)*S)
    else:
        B_price = Q
    print(f"#{tc} ",end="")

    if A_price < B_price:
        print(A_price)
    else:
        print(B_price)