t = int(input())
for tc in range(1, t+1):
    for n in range(0, 10):
        a = list(map(int, input().split()))
        all_list = 0
        all_list.append(a)
        for i in range(0, 10):
            for j in range(0, 10):
                b = all_list[i][j]
                if len(set(b)) == 9:
                    print()
