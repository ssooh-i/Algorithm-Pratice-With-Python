T = int(input())
for tc in range(1, T+1):
    A, B= map(int, input().split())
    print(f"#{tc} ",end ="")
    if A > B:
        print(">")
    elif A < B:
        print("<")
    else:
        print("=")