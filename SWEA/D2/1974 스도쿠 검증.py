T = int(input())


def check(arr):
    # 가로 확인
    for i in range(9):

        check = []
        for j in range(9):
            if check:
                if arr[i][j] in check:
                    return '0'
            check.append(arr[i][j])

    # 세로 확인
    for i in range(9):
        check = []
        for j in range(9):
            if check:
                if arr[j][i] in check:
                    return '0'
            check.append(arr[j][i])

    # 블록 확인
    for i in range(0, 9, 3):  # 시작점
        for j in range(0, 9, 3):
            check = []

            # 블록
            for k in range(3):
                for t in range(3):
                    if check:
                        if arr[i + k][j + t] in check:
                            return '0'
                    check.append(arr[i + k][j + t])
    return '1'


for tc in range(1, T + 1):
    arr = [list(map(int, input().split())) for _ in range(9)]
    print("#{}".format(tc), end=' ')
    print(check(arr))

# t = int(input())
# for tc in range(1, t + 1):
#     n = list(map(int, input().split(" ")))
#     n_list = [] #9*9 스도쿠 리스트 들어갈 곳
#     for i_n in range(0, 10):
#         _n = list(map(int, input().split(" ")))
#         n_list.append(_n) #9개씩 잘라져서 들어감
#         print(*n_list)
#
#         result = False
#         sum = 0 #스도쿠 한구역 검사한 자리
#
#         #세로줄 검증
#         for i in range(0,10):
#             for j in range(0,10):
#                 sum += int(n_list[i][j])
#                 if sum == 45:
#                     result = True
#                 else:
#                     print(0)
#
#         #가로줄 검증
#         for i in range(0,10):
#             for j in range(0,10):
#                 sum += int(n_list[j][i])
#                 if sum == 45:
#                     result = True
#                 else:
#                     print(0)
#
#         print(result)




    # m_list = []
    # for i in range(n - m + 1):
    #     for j in range(n - m + 1):
    #         count = 0
    #         for x in range(n):
    #             for y in range(m):
    #                 count += n_list[i + x][j + y]
    #         m_list.append(count)
    # m_list.sort()
    # print(f"#{tc} {m_list[-1]}")

    # all_list = []
    # for n in range(0, 10):
    #     a = list(map(int, input().split()))
    #     all_list.append(a)
    #     for i in range(0, 10):
    #         for j in range(0, 10):
    #             b = all_list[i][j]
    #             if len(set(b)) == 9:
    #                 print()
