t = int(input())
for tc in range(1, t+1):
    n = int(input())
    arr_len = n*n
    arr = []
    for i in range(1, arr_len+1):
        arr.append(i)
    print(arr)
    matrix = [[0 for _ in range(n)] for _ in range(n)] #n*n배열 0으로 초기화

    #matrix.insert(index번호, 값)
    for i in range(0, n, 1):
        for j in range(0, n, 1):
            for x in range(1, arr_len+1):
            #matrix[i][j] = arr(i)
                matrix[i][j] = x

    print(matrix)
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