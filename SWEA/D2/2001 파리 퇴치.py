def summing(flys, startY, startX, M):
    _sum = 0

    for i in range(startY, startY+M):
        for j in range(startX, startX+M):
            _sum += flys[i][j]

    return _sum

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())

    flys = [[0 for _ in range(N)] for _ in range(N)]

    for i in range(N):
        _input = list(map(int, input().split()))
        for j in range(len(_input)):
            flys[i][j] = _input[j]

    _max = 0
    for i in range(0, N - M + 1):
        for j in range(0, N - M + 1):
            _max = max(_max, summing(flys, i, j, M))

    print(f"#{tc} {_max}")

# t = int(input())
# for tc in range(1, t+1):
#     n, m = map(int,input().split(" "))
#     n_list = []
#     for i_n in range(0, n):
#         _n = list(map(int, input().split(" ")))
#         n_list.append(_n)
#     print(*n_list)
#     m_list = []
#     for i in range(n-m+1):
#         for j in range(n-m+1):
#             count = 0
#             for x in range(n):
#                 for y in range(m):
#                     count += n_list[i+x][j+y]
#             m_list.append(count)
#     m_list.sort()
#     print(f"#{tc} {m_list[-1]}")
#
