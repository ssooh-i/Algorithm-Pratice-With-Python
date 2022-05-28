def rotate90(arr):
    arr2 = [[0 for _ in range(N)] for _ in range(N)]
    for y in range(N):
        for x in range(N):
            arr2[x][N-1-y] = arr[y][x]
    return arr2

T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = []
    for _ in range(N):
        arr.append(list(map(int, input().split())))
    arr2 = rotate90(arr)
    arr3 = rotate90(arr2)
    arr4 = rotate90(arr3)
    total = [arr2, arr3, arr4]

    print(f"#{tc}")
    for r in range(N):
        for i in range(3):
            for c in range(N):
                print(total[i][r][c], end="")
            print(end=" ")
        print()
    