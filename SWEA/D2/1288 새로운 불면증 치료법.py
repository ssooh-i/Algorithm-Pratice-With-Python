T = int(input())

for t in range(1, 1+T):
    N = input()
    arr = [0,0,0,0,0,0,0,0,0,0]
    intN = int(N)
    count = 1
    while 0 in arr:
        for i in N:
            if arr[int(i)] > 0:
                continue
            else:
                arr[int(i)] += 1
        count += 1
        result = str(intN*count)
    count -= 1
    print(f'#{t} {result}')
