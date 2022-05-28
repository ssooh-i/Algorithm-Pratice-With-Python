T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    #달팽이 진행 방향: 동 남 서 북
    dy = [0, 1, 0, -1]
    dx = [1, 0, -1, 0]
    #현재 위치
    now_y = 0
    now_x = 0
    #현재진행 방향
    D = 0
    print(f"#{tc}")
    for i in range(1, (N*N)+1):

        matrix[now_y][now_x] = i
        next_y = now_y + dy[D]
        next_x = now_x + dx[D]

        if ((next_y >= N) or (next_x >= N))\
                or ((next_y < 0) or (next_x < 0))\
                or (matrix[next_y][next_x] != 0):
            if D == 3:
                D = 0
            else:
                D += 1
        # elif (next_y < 0) or (next_x < 0):
        #     if D == 3:
        #         D = 0
        #     else:
        #         D += 1
        # elif matrix[next_y][next_x] != 0:
        #     if D == 3:
        #         D = 0
        #     else:
        #         D += 1

        now_y += dy[D]
        now_x += dx[D]

    for i in range(N):
        for j in range(N):
            print(matrix[i][j], end=" ")
        print()

