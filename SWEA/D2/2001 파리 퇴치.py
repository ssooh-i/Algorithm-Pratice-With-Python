t = int(input())
for tc in range(1, t+1):
    n, m = map(int,input().split(" "))
    n_list = []
    for i_n in range(0, n):
        _n = list(map(int, input().split(" ")))
        n_list.append(_n)
    print(*n_list)
    m_list = []
    for i in range(n-m+1):
        for j in range(n-m+1):
            count = 0
            for x in range(n):
                for y in range(m):
                    count += n_list[i+x][j+y]
            m_list.append(count)
    m_list.sort()
    print(f"#{tc} {m_list[-1]}")

