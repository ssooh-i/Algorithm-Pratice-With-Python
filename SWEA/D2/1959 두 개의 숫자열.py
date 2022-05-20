t = int(input())
for tc in range(1, t+1):
    A, B = map(int, input().split(" "))
    arr_A = list(map(int, input().split(" ")))
    arr_B = list(map(int, input().split(" ")))
    _max = 0

    if B > A:
        for i in range(0, B-A+1):
            sum = 0
            for j in range(A):
                sum += arr_B[j+i] * arr_A[j]
            _max = max(_max, sum)

    elif A > B:
        for i in range(0, A-B+1):
            sum = 0
            for j in range(B):
                sum += arr_A[j+i] * arr_B[j]
            _max = max(_max, sum)

    else: #A == B
        sum = 0
        for i in range(0, A):
            sum += arr_A[i] * arr_B[i]
            _max = sum

    print(f"#{tc} {_max}")