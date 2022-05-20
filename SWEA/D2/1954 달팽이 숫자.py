t = int(input())

for tc in range(1, t+1):
    n = int(input())
    arr_len = n*n
    matrix = [[0 for _ in range(n)] for _ in range(n)] # n * n 배열 0으로 초기화

    value = 1
    for i in range(0, n):
        matrix[0][i] = value
        value+=1
    for i in range(1, n):
        matrix[i][n-1] = value
        value += 1
    for i in range(n-2, -1, -1):
        matrix[n-1][i] = value
        value += 1
    for i in range(n-2, 0, -1):
        matrix[i][0] = value
        value += 1

    # 동, 남, 서, 북
    dy = [0, 1, 0, -1] # y축으로의 방향
    dx = [1, 0, -1, 0] # x축으로의 방향
    d = 0 # 현재 진행방향
    nowY = 1
    nowX = 1

    for _value in range(value, n*n+1):
        matrix[nowY][nowX] = _value

        if matrix[nowY+dy[d]][nowX+dx[d]] != 0:
            if d == 3:
                d = 0
            else:
                d+=1

        nowY += dy[d]
        nowX += dx[d]
    print(f"#{tc}")

    for i in matrix:  # matrix에서 안쪽 리스트를 꺼냄
        for j in i:  #안쪽 리스트에서 요소를 하나씩 꺼냄
            print( j, end=' ')
        print()

# t = int(input())
# for tc in range(1, t+1):
#     n = int(input())
#     arr_len = n*n
#     arr = []
#     for i in range(1, arr_len+1):
#         arr.append(i)
#     print(arr)
#     matrix = [[0 for _ in range(n)] for _ in range(n)] #n*n배열 0으로 초기화
#
#     #matrix.insert(index번호, 값)
#     for i in range(0, n, 1):
#         for j in range(0, n, 1):
#             for x in range(1, arr_len+1):
#             #matrix[i][j] = arr(i)
#                 matrix[i][j] = x
#
#     print(matrix)
    #
    # matrix = []
    # for i in range(0, n*n+1):
    #     #inputMatrix = list(map(int, input().split()))
    #     inputMatrix = i
    #     matrix.append(inputMatrix)
    #
    # for i in range(0, n):
    #     for j in range(0, n):
    #         print(matrix[i][j], end=' ')
    #     print(matrix)