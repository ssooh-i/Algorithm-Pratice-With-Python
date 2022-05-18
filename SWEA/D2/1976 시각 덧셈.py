t = int(input())
for tc in range(1, t+1):
    times = list(map(int, input().split()))
    h = (times[0]+times[2])
    m = (times[1]+times[3])
    if m >= 60:
        h = h+1
        m = m-60
    if h > 12:
        h = h-12

    print(f"#{tc} {h} {m}")
