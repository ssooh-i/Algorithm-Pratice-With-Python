T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    now_x = 0  # 현재 위치
    now_y = 0
    # 동 남 서 북
    dy = [0, 1, 0, -1]  # y축
    dx = [1, 0, -1, 0]  # x축
    D = 0

    for i in range(1, N * N + 1):
        matrix[now_y][now_x] = i

        next_y = now_y + dy[D]
        next_x = now_x + dx[D]

        if (next_y >= N) or (next_x >= N):
            if D == 3:
                D = 0
            else:
                D += 1
        elif (next_y < 0) or (next_x < 0):
            if D == 3:
                D = 0
            else:
                D += 1
        elif matrix[next_y][next_x] != 0:
            if D == 3:
                D = 0
            else:
                D += 1

        now_y += dy[D]
        now_x += dx[D]
    print(f"#{tc}")
    for i in range(0, N):
        for j in range(0, N):
            print(matrix[i][j], end=" ")
        print()