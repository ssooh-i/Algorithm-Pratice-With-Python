T = int(input())
for tc in range(1, T+1):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]

    # 우, 하, 왼, 상
    dy = [0, 1, 0, -1] # y축방향
    dx = [1, 0, -1, 0] # x축방향

    for i in range(N):
        for j in range(N):
            '''
            0이 아닌 숫자라면 방향 전환
            0이라면 숫자 추가
            '''
