T = int(input())
for tc in range(1, T+1):
    N, M = map(int,input().split())
    arr = [list(map(int, input().split())) for _ in range(N)]
    _max = 0
    for i in range(0, N-M-1): #인덱스에러 안나게 N-M-1해줌
        for j in range(0, N-M-1):
            sum_flys = 0
            for x in range(M): #M*M범위안 파리 합치기
                for y in range(M):
                    sum_flys += arr[i+x][j+y]
            if _max < sum_flys:
                _max = sum_flys
    print(f"#{tc} {_max}")
    
#테스트케이스 10개중에 4개만 맞음// 오답됨