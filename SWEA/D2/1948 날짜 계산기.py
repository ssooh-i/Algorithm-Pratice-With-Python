t = int(input())
days = {1: 31, 2:28, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31} #딕셔너리형은 {} 형태
for tc in range(1, t+1):
    m1, d1, m2, d2 = map(int, input().split())
    day = 0
    m = 0
    if m1 == m2:
        day = d2 - d1 + 1
    else:
        #m2 최대 날짜 - d2 + d1
        day += (days[m1]-d1)
        for i in range(m1+1, m2):
            day += days[i]
        day += d2

        # if d2 > d1:
        #     d2 = days[m2] - d2
        #     #d1 = days[m1] - d1
        #     # print(days[m2], d2)
        #     day = m - (d2 + d1) + 1
        #d1이  d2보다 더 클 때를 식만들어줘야댐


    print(f"#{tc} {day}")