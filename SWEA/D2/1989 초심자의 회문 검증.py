t = int(input())
for tc in range(1, t+1):
    arr = list(input())
    arr2 = list(reversed(arr))
    print(f"#{tc} ", end="")
    if arr == arr2:
        print(str(1))
    else:
        print(str(0))