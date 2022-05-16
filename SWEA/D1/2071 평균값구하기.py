T = int(input())
med = 0
for i in range(1, T+1):
    list_t = list(map(int, input().split(" ")))
    if len(list_t) == 10:
        med = sum(list_t)/10
        print("#"+str(i), round(med))
#round():사사오입원칙(반올림할 자리수가 5이면 반올림할 때 앞자리 숫자가 짝수면 내림, 홀수면 올림)을 따름
#
    else:
        print(-1)