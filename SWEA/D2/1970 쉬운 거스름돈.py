t = int(input())
for tc in range(1, t+1):
    N = int(input())
    money = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    change = [0 for _ in range(8)]
    print(f"#{tc}")
    for i in range(8):
        if N//money[i] > 0:
            change[i] += N//money[i]
            N = N % money[i]
    print(*change)

#https://velog.io/@shon4bw/SWEA-1970-%EC%89%AC%EC%9A%B4-%EA%B1%B0%EC%8A%A4%EB%A6%84%EB%8F%88-%ED%8C%8C%EC%9D%B4%EC%8D%AC
#참고