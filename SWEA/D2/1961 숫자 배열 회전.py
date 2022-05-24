def Degrees90(arr, N):
    arr2 = []
    for i in range(0, N):
        for j in range(N-1, -1, -1):
            arr2.append(arr[j][i])
    return arr2

def Degrees180(arr,N):
    arr2 = []
    for i in range(N-1, -1, -1):
        for j in range(N-1, -1, -1):
            arr2.append(arr[i][j])
    return arr2

def Degrees270(arr, N):
    arr2 = []
    for i in range(N-1, -1, -1):
        for j in range(0, N):
            arr2.append(arr[j][i])
    return arr2

T = int(input())

for tc in range(T):
    N = int(input())
    arr = []
    for i in range(N):
        a = list(map(int, input().split()))
        arr.append(a)

    A = Degrees90(arr, N)
    B = Degrees180(arr, N)
    C = Degrees270(arr, N)

    arr3 = [A, B, C]
    arr4 = sum(arr3, []) #2차원배열->1차원배열로만듦
    arr5 = []
    arr6 = []

    for i in range(0, len(arr4), N):
        arr5.append(arr4[i:i+3])

    # for i in range(0,N):
    #     for j in range(0, N):
    #         print(arr5[j][i])

    print(arr5)
